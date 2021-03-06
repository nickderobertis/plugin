const fs = require('fs');
const dataStr = fs.readFileSync(process.stdin.fd, 'utf-8');
const data = JSON.parse(dataStr);
const {args, kwargs} = data;
var {value} = kwargs;
value += 20;
const result = { args: [], kwargs: {value}};
process.stdout.write(JSON.stringify(result));