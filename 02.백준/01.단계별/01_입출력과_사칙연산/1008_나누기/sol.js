const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

rl.question('', (input) => {
  const inputData = input.split(' ')
  const A = parseInt(inputData[0])
  const B = parseInt(inputData[1])
  console.log(A/B)

  rl.close()
})