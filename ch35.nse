description = [[
 Determines if port is open
]]

author = "Yue"

portrule = function(host, port)
 return port.protocol == "tcp"
 and port.state == "open"
end

action = function(host, port)
 return "Port is open"
end
