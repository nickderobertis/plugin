const fs = require('fs');
const dataStr = fs.readFileSync(process.stdin.fd, 'utf-8');
const data = JSON.parse(dataStr);
const {args, kwargs} = data;
var {value2} = kwargs;
value2 += 20;
const result = { args: args[0] + 20, kwargs: {value2}};
process.stdout.write(JSON.stringify(result));