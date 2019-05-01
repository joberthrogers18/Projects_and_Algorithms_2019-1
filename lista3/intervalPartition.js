//const Heap = require("heap");

const BinaryHeap = require('@tyriar/binary-heap');

all_times = [{ "start": '01:25', "final": '06:40' }, { "start": '07:45', "final": '10:45' }, { "start": '11:30', "final": '20:40' }]

//last_time = new Heap();

/*let date1 = new Date()
let date2 = new Date()
date1.setHours(1, 12)
date2.setHours(2,30)*/

/*let heap = new Heap()
heap.push(date1)
heap.push(date2)*/

const intervalPartition = (time) => {

    let heap = new BinaryHeap();
    let heapEarlyEnd = new BinaryHeap();
    let classes = []

    time.map((current, key) => {
        heap.insert(current.final, key)
    })

    while (!heap.isEmpty()) {

        console.log(heap.findMinimum());

        if (classes.length === 0) {

            aux = []
            let node = heap.extractMinimum();
            aux.push(time[node.value]);
            heapEarlyEnd.insert(node.key, 0);
            classes.push(aux);
        } else {
            console.log('----------------------------')
            if(heapEarlyEnd.findMinimum().key <= heap.findMinimum().key){
                let node = heap.extractMinimum();
                let currentEarly = heapEarlyEnd.extractMinimum()
                classes[currentEarly.value].push(time[node.value]);
                heapEarlyEnd.insert(time[node.value].final , currentEarly.value);
            }
            
            //let nodeAux = heap.extractMinimum();

        }

    }

    console.log(classes);
    console.log(heapEarlyEnd)
}

intervalPartition(all_times)

//console.log(last_time.peek())

/*
console.log(heap)

let currentDate = heap.pop();

console.log(currentDate.getHours())

currentDate = heap.pop()

console.log(currentDate)*/
