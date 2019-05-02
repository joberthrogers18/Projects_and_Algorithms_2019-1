const BinaryHeap = require('@tyriar/binary-heap');

module.exports= {
  intervalPartition(req, res){

        var date = new Date();

        time = [{ "start": new Date(date.setHours(01,05)), "final":new Date( date.setHours(06, 15)) }, { "start": new Date(date.setHours(05,30)), "final": new Date(date.setHours(10,10)) }, { "start": new Date(date.setHours(11,50)), "final": new Date(date.setHours(20,45)) },
        { "start": new Date(date.setHours(02,30)) , "final": new Date(date.setHours(07,25)) }, { "start": new Date(date.setHours(20,23)) , "final": new Date(date.setHours(21,20)) }, { "start": new Date(date.setHours(15,10)), "final": new Date(date.setHours(23,05)) }]

        let heap = new BinaryHeap();
        let heapEarlyEnd = new BinaryHeap();
        let classes = []

        time.map((current, key) => {
            heap.insert(current.start, key)
        })

        while (!heap.isEmpty()) {

            if (classes.length === 0) {

                aux = []
                let node = heap.extractMinimum();
                aux.push(time[node.value]);
                classes.push(aux);
                heapEarlyEnd.insert(time[node.value].final, 0);

            } else {
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
                

            }

        }

        res.json(classes);

    }

}


