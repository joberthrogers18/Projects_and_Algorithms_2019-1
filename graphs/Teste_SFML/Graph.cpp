#include <iostream>
#include <list>
#include <queue>

using namespace std;

class Graph {

private:
	int V;
	list<int> *adj;
public:
	Graph(int V) {
		this->V = V; //number of nodes
		adj = new list<int>[V];
	}

	void addEdge(int v, int w);
	void BSF(int s, bool visited[]);
	Graph getTransport();
	bool isConnected();

};

//Adding the edge in list adjacent of both nodes
void Graph::addEdge(int v, int w)
{
	adj[v].push_back(w);
	adj[w].push_back(v);
}

// Function to BSF using recursion

void Graph::BSF(int s, bool visited[]) {

	list<int> q; // create the list of neigbohoods and
	list<int>::iterator i;
	visited[s] = true; // mark as visited
	q.push_back(s); // adding the curent like visited


	while (!q.empty()) {

		int aux = s;
		s = q.front(); //take the first in list
		q.pop_front();

		cout << s << " neighbor of " << aux << "\n";

		for (i = adj[s].begin(); i != adj[s].end(); i++) {

			if (!visited[*i]) {
				visited[*i] = true;
				q.push_back(*i);
			}
		}
	}


}


/*int main() {

	bool visited[4];
	Graph g(4);
	g.addEdge(0, 1);
  g.addEdge(0, 2);
  g.addEdge(1, 2);
  g.addEdge(2, 3);
  g.addEdge(3, 3);
	g.BSF(0, visited);

	return 0;
}*/