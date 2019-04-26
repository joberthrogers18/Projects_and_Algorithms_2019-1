const Heap = require("heap");

let date1 = new Date()
let date2 = new Date()
date1.setHours(1, 12)
date2.setHours(2,30)

let heap = new Heap()
heap.push(date1)
heap.push(date2)

console.log(heap)

let currentDate = heap.pop();

console.log(currentDate.getHours())

currentDate = heap.pop()

console.log(currentDate)
