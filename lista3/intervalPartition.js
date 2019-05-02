//const Heap = require("heap");

const BinaryHeap = require('@tyriar/binary-heap');

all_times = [{ "start": '01:25', "final": '06:40' }, { "start": '05:45', "final": '10:45' }, { "start": '11:30', "final": '20:40' },
{ "start": '02:00', "final": '07:00' }, { "start": '20:10', "final": '21:00' }, { "start": '15:00', "final": '23:10' }]

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
            console.log('--------------');
            console.log(heapEarlyEnd.findMinimum().key)
            console.log(heap.findMinimum().key)
            if(heapEarlyEnd.findMinimum().key <= time[heap.findMinimum().value].start){
                let node = heap.extractMinimum();
                let currentEarly = heapEarlyEnd.extractMinimum()
                classes[currentEarly.value].push(time[node.value]);
                heapEarlyEnd.insert(time[node.value].final , currentEarly.value);
            }
            else{
                let node = heap.extractMinimum();
                aux = [];
                aux.push(time[node.value]);
                classes.push(aux);
                heapEarlyEnd.insert(node.key,classes.length - 1);
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
