n = 6040
m = 3883

require "nn"
mlp = nn.Linear(n+m, 1)
criterion = nn.MSECriterion()

function mysplit(inputstr, sep)
	if sep == nil then
		sep = "%s"
        end
        local t={} ; i=1
        for str in string.gmatch(inputstr, "([^"..sep.."]+)") do
                t[i] = str
                i = i + 1
        end
        return t
end

local cnt = 0

local trainFile = io.open("../rowcol/train.rc3", "r")
for line in trainFile:lines() do
	cnt = cnt + 1
	if cnt % 10000 == 0 then
		print(cnt)
	end

	if torch.uniform() < 0.001 then
		local t = mysplit(line, " ")
	
		local x = {}
		for i = 1, n+m do
			x[i] = 0
		end
		for i = 2, #t do
			tt = mysplit(t[i], ":")
			index = tonumber(tt[1])
			value = tonumber(tt[2])
			x[index] = value
		end
	
		local y = { tonumber(t[1]) }
		
		local input = torch.Tensor(x);
		local output = torch.Tensor(y);

		
		local predict = mlp:forward(input)
		local err = criterion:forward(predict, output)
		
		print(err)
		mlp:zeroGradParameters()

		local gradient = criterion:backward(predict, output)
		mlp:backward(input, gradient)
		
		mlp:updateParameters(0.01)

		local _output = mlp:forward(input)

        	--print(input)
        	print(math.abs(output[1] - _output[1]))

	end
end
trainFile:close()

local err = 0
cnt = 0

local testFile = io.open("../rowcol/test.rc3", "r")
for line in testFile:lines() do
        local t = mysplit(line, " ")

        local x = {}
	for i = 1, n+m do
		x[i] = 0
	end
        for i = 2, #t do
                tt = mysplit(t[i], ":")
                index = tonumber(tt[1])
                value = tonumber(tt[2])
                x[index] = value
        end

        local y = { tonumber(t[1]) }

        local input = torch.Tensor(x);
        local output = torch.Tensor(y);

	local _output = mlp:forward(input)

	--print(input)
	--print(output)
	--print(_output)

	err = err + (output[1] - _output[1]) ^ 2
	cnt = cnt + 1
	break
end
testFile:close()

err = math.sqrt(err / cnt)
--print(err)

