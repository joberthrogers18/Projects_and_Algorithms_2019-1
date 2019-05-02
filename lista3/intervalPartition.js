//const Heap = require("heap");

const BinaryHeap = require('@tyriar/binary-heap');

all_times = [{ "start": 01, "final": 06 }, { "start": 05, "final": 10 }, { "start": 11, "final": 20 },
{ "start": 02 , "final": 07 }, { "start": 20 , "final": 21 }, { "start": 15, "final": 23 }]

const intervalPartition = (time) => {

    let heap = new BinaryHeap();
    let heapEarlyEnd = new BinaryHeap();
    let classes = []

    time.map((current, key) => {
        heap.insert(current.start, key)
    })

    while (!heap.isEmpty()) {

        console.log(heap.findMinimum());

        if (classes.length === 0) {

            aux = []
            let node = heap.extractMinimum();
            aux.push(time[node.value]);
            classes.push(aux);
            heapEarlyEnd.insert(time[node.value].final, 0);

        } else {
            console.log('--------------');
            console.log(time[heapEarlyEnd.findMinimum().value].final)
            console.log(time[heap.findMinimum().value].start)
            if(time[heapEarlyEnd.findMinimum().value].final <= time[heap.findMinimum().value].start){
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
                heapEarlyEnd.insert(time[node.value].final,classes.length - 1);
            }
            
            //let nodeAux = heap.extractMinimum();

        }

    }

    console.log(classes);
    console.log(heapEarlyEnd)
    console.log(heap)
}

intervalPartition(all_times)

//console.log(last_time.peek())

/*
console.log(heap)

let currentDate = heap.pop();

console.log(currentDate.getHours())

currentDate = heap.pop()

console.log(currentDate)*/
