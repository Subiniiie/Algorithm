const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './브론즈2/2747_피보나치_수/example.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

var n = Number(input[0])
var dp = []
for (let i=0; i <= n; i++) {
    if (i === 0) {
        dp.push(0)
    } else if (i === 1 || i === 2) {
        dp.push(1)
    } else {
        dp.push(dp[i-1] + dp[i-2])
    }
}
dp[1] = 1
dp[2] = 1


if (n === 1 || n === 2) {
    console.log(1)
} else {
    console.log(dp[n])
}