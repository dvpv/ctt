const grpc = require("grpc");
const protoLoader = require("@grpc/proto-loader");

const packageDefinition = protoLoader.loadSync("../proto/hello.proto", {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
});
const example_proto = grpc.loadPackageDefinition(packageDefinition).hello;

function sayHello(call, callback) {
  const response = {
    message: "Hello, " + call.request.name,
  };
  callback(null, response);
}

const server = new grpc.Server();
server.addService(example_proto.HelloService.service, { SayHello: sayHello });

server.bind("0.0.0.0:50051", grpc.ServerCredentials.createInsecure());
console.log("Server running at http://0.0.0.0:50051");
server.start();
