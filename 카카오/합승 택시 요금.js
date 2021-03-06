function solution(n, s, a, b, fares) {
    
    function floyd_warshall(graph) {
        for (let k=0; k < graph.length; k++) {
            for (let i=0; i < graph.length; i++) {
                for (let j=0; j < graph.length; j++) {
                    if (graph[i][j] > graph[i][k] + graph[k][j]) graph[i][j] = graph[i][k] + graph[k][j]
                }
            }
        }
        return graph
    }

    var inf = Infinity;
    var answer = inf;
    var graph = Array.from(Array(n+1), () => new Array(n+1).fill(inf));

    for (let i = 0; i < n+1; i++) {
        graph[i][i] = 0
    }
    
    for(var value of fares) {
        graph[value[0]][value[1]] = value[2]
        graph[value[1]][value[0]] = value[2]
    };


    graph = floyd_warshall(graph);

    for (let i = 0; i < n+1; i++) {
        if (answer > graph[s][i] + graph[i][a] + graph[i][b])
            answer = graph[s][i] + graph[i][a] + graph[i][b]
    }  

    answer = Math.min(answer, graph[s][a] + graph[a][b], graph[s][b] + graph[b][a])
    return answer
}