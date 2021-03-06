const fs = require('fs');
const dataStr = fs.readFileSync(process.stdin.fd, 'utf-8');
const data = JSON.parse(dataStr);
const {args, kwargs} = data;

const result = { args: [args[0] + 20, args[1] + 20], kwargs: {}};
process.stdout.write(JSON.stringify(result));