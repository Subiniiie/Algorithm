const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(process.platform === 'linux' ?
    '/dev/stdin' : path.join(__dirname, "input.txt")
).toString().split("\n").map((el) => el.split(" ").map(Number));

let N = input[0][0];
const heap = [];


function swap(i, j) { [heap[i], heap[j]] = [heap[j], heap[i]]; }

function push(x) {
    heap.push(x);

    for (let i = heap.length - 1; i > 1 && heap[i >> 1] > heap[i]; i >>= 1)
        swap(i, i >> 1);
}

function popMin() {                  // 힙 크기가 N+1일 때만 호출
  const min = heap[1];
  heap[1] = heap.pop();
  for (let i = 1, len = heap.length; ;) {
    let l = i << 1, r = l + 1, small = i;
    if (l < len && heap[l] < heap[small]) small = l;
    if (r < len && heap[r] < heap[small]) small = r;
    if (small === i) break;
    swap(i, small);  i = small;
  }
  return min;
}

for (let i = 1; i < N + 1; i++) {
    push(input[i]);

    if (heap.length - 1 > N) popMin();
};

console.log(heap[1]);

