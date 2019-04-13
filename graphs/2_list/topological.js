function topo(dependences){
   
    const sorted = [];
    const visited = {};

    for(const elem of Object.keys(dependences)){
        toposorted(elem, dependences, sorted, visited);
    }

    sorted.reverse();
    return sorted;
}

function toposorted(elem, dependences, sorted, visited){
    if(visited[elem]){
        return;
    }

    visited[elem] = true;

    dependence_iterable = dependences[elem];

    for(const dependence of dependence_iterable){
        toposorted(dependence, dependences, sorted, visited);
    }
    
    sorted.push(elem)
}

/*
    A -> E
    B -> D
    C -> D
    E -> F
    D -> F
*/

let dependences = {
    A: ['E'],
    B: ['D', 'G'],
    C: ['D'],
    E: ['F'],
    D: ['F'],
    F: [],
    G: []
}

const array_topological = topo(dependences);
console.log(array_topological);

// Using TDD
// A, B, C, E, D, F ---> true
// A, F ---> False
/*
function check(dependences, sorted){
    for(let i = 0; i < sorted.length; i++){
        for(let dependences of dependences[sorted[i]]){
            for(let j = i -1; j > 0; j++){
                if(dependences === sorted[j]){
                    return false;
                }
            }
        }
    }
    for(let eleme)
}*/