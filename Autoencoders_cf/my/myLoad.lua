require("sys")
require("torch")

torch.setdefaulttensortype('torch.FloatTensor')

require("nnsparse")


function preprocess(x)
    return (x-3)/2
end

function postprocess(x)
    return 2*x+3
end

function appendTrain(userId, itemId, rating)
    -- bufferize sparse tensors
    if data.train.U.data[userId] == nil then data.train.U.data[userId] = nnsparse.DynamicSparseTensor(200) end
    if data.train.V.data[itemId] == nil then data.train.V.data[itemId] = nnsparse.DynamicSparseTensor(200) end

    data.train.U.data[userId]:append(torch.Tensor{itemId, rating})
    data.train.V.data[itemId]:append(torch.Tensor{userId, rating})

    --update the training mean
    data.__noRating = data.__noRating + 1
    data.__n    =  data.__n + 1
    data.__mean = (data.__n*data.__mean + rating) / ( data.__n + 1 )

    --store the matrix size by keeping the max Id
    data.__Usize = math.max(data.__Usize, userId)
    data.__Vsize = math.max(data.__Vsize, itemId)
end

function appendTest(userId, itemId, rating)
    -- bufferize sparse tensors
    if data.test.U.data[userId] == nil then data.test.U.data[userId] = nnsparse.DynamicSparseTensor.new(200) end
    if data.test.V.data[itemId] == nil then data.test.V.data[itemId] = nnsparse.DynamicSparseTensor.new(200) end

    data.test.U.data[userId]:append(torch.Tensor{itemId, rating})
    data.test.V.data[itemId]:append(torch.Tensor{userId, rating})

    data.__noRating = data.__noRating + 1

    --store the matrix size by keeping the max Id
    data.__Usize = math.max(data.__Usize, userId)
    data.__Vsize = math.max(data.__Vsize, itemId)
end


data = {}
data.train = { U = { data = {}, info = {} }, V = { data = {}, info = {} } }
data.test  = { U = { data = {}, info = {} }, V = { data = {}, info = {} } }

data.__Usize = 0
data.__Vsize = 0
data.__mean  = 0
data.__n     = 0

data.__noRating = 0


local trainFile = io.open("../../data/my/train.txt", "r")
for line in trainFile:lines() do
    local userIdStr, movieIdStr, ratingStr = line:match('(%d+) (%d+) (%d%.?%d?)')

    local userId  = tonumber(userIdStr)
    local itemId  = tonumber(movieIdStr)
    local rating  = tonumber(ratingStr)

    rating = preprocess(rating)

    appendTrain(userId, itemId, rating)
end
trainFile:close()


local testFile = io.open("../../data/my/test.txt", "r")
for line in testFile:lines() do
    local userIdStr, movieIdStr, ratingStr = line:match('(%d+) (%d+) (%d%.?%d?)')

    local userId  = tonumber(userIdStr)
    local itemId  = tonumber(movieIdStr)
    local rating  = tonumber(ratingStr)

    rating = preprocess(rating)

    appendTest(userId, itemId, rating)
end
testFile:close()


print(data.__Usize)
print(data.__Vsize)
print(data.__mean)
print(data.__n)
print(data.__noRating)


local function build(X)
    for k, x in pairs(X.data) do
        X.data[k] = torch.Tensor.ssortByIndex(x:build())
    end
end

build(data.train.U)
build(data.train.V)
build(data.test.U)
build(data.test.V)


--store mean, globalMean and std for every row/column
local function computeBias(X, gMean)
    for k, x in pairs(X.data) do
        X.info[k] = X.info[k] or {}
        X.info[k].mean  = x[{{},2}]:mean()
        X.info[k].std   = x[{{},2}]:std()
        X.info[k].gMean = gMean
    end
end

computeBias(data.train.U, data.__mean)
computeBias(data.train.V, data.__mean)

--Provide external information
data.train.U.info.size, data.test.U.info.size = data.__Usize, data.__Usize
data.train.V.info.size, data.test.V.info.size = data.__Vsize, data.__Vsize

data.train.U.info.dimension, data.test.U.info.dimension = data.__Vsize, data.__Vsize
data.train.V.info.dimension, data.test.V.info.dimension = data.__Usize, data.__Usize

data.train.U.info.noRating, data.test.U.info.noRating = data.__n, data.__noRating - data.__n
data.train.V.info.noRating, data.test.V.info.noRating = data.__n, data.__noRating - data.__n


local cnt = 0
for i = 1, 6040 do
	if data.train.U.data[i] ~= nil then
		cnt = cnt + 1
	end
end
print(cnt)

local cnt = 0
for i = 1, 3883 do
	if data.train.V.data[i] ~= nil then
		cnt = cnt + 1
	end
end
print(cnt)

local cnt = 0
for i = 1, 6040 do
	if data.test.U.data[i] ~= nil then
		cnt = cnt + 1
	end
end
print(cnt)

local cnt = 0
for i = 1, 3883 do
	if data.test.V.data[i] ~= nil then
		cnt = cnt + 1
	end
end
print(cnt)



torch.save("newTrain.t7", {train = data.train, test = data.test })



