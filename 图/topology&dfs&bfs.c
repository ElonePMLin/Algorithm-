// 拓扑排序
// emplace、emplace_back STL 的方法 "放置"
class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if (n == 1) {
            return {0};
        }
        vector<vector<int>> nodes(n);
        vector<int> degree(n, 0);
        for (auto &e : edges) {
            nodes[e[0]].emplace_back(e[1]);
            nodes[e[1]].emplace_back(e[0]);
            degree[e[1]]++;
            degree[e[0]]++;
        }
        queue<int> q;
        vector<int> ans;
        for (int i = 0; i < n; i++) {
            if (degree[i] == 1) q.emplace(i);
        }

        while (n > 2) {
            int s = q.size();
            n -= s;
            for (int i = 0; i < s; i++) {
                int curr = q.front();  // queue.front() 取队头，右侧为队头
                q.pop();  // queue.pop() 退队，右侧为队头
                for (auto &node : nodes[curr]) {
                    if (--degree[node] == 1) q.emplace(node);
                }
            }
        }

        while (!q.empty()) {
            ans.emplace_back(q.front());
            q.pop();
        }
        return ans;
    }
};

// dfs
class Solution {
public:
    void dfs(int u, vector<int> & dist, vector<int> & parent, const vector<vector<int>> & adj) {
        for (auto & v : adj[u]) {
            if (dist[v] < 0) {
                dist[v] = dist[u] + 1;
                parent[v] = u;
                dfs(v, dist, parent, adj);
            }
        }
    }

    int findLongestNode(int u, vector<int> & parent, const vector<vector<int>> & adj) {
        int n = adj.size();
        vector<int> dist(n, -1);
        dist[u] = 0;
        dfs(u, dist, parent, adj);
        int maxdist = 0;
        int node = -1;
        for (int i = 0; i < n; i++) {
            if (dist[i] > maxdist) {
                maxdist = dist[i];
                node = i;
            }
        }
        return node;
    }

    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if (n == 1) {
            return {0};
        }
        vector<vector<int>> adj(n);
        for (auto & edge : edges) {
            adj[edge[0]].emplace_back(edge[1]);
            adj[edge[1]].emplace_back(edge[0]);
        }
        vector<int> parent(n, -1);
        /* 找到距离节点 0 最远的节点  x */
        int x = findLongestNode(0, parent, adj);
        /* 找到距离节点 x 最远的节点  y */
        int y = findLongestNode(x, parent, adj);
        /* 找到节点 x 到节点 y 的路径 */
        vector<int> path;
        parent[x] = -1;
        while (y != -1) {
            path.emplace_back(y);
            y = parent[y];
        }
        int m = path.size();
        if (m % 2 == 0) {
            return {path[m / 2 - 1], path[m / 2]};
        } else {
            return {path[m / 2]};
        }
    }
};


// bfs
class Solution {
public:
    int findLongestNode(int u, vector<int> & parent, vector<vector<int>>& adj) {
        int n = adj.size();
        queue<int> qu;
        vector<bool> visit(n);
        qu.emplace(u);
        visit[u] = true;
        int node = -1;

        while (!qu.empty()) {
            int curr = qu.front();
            qu.pop();
            node = curr;
            for (auto & v : adj[curr]) {
                if (!visit[v]) {
                    visit[v] = true;
                    parent[v] = curr;
                    qu.emplace(v);
                }
            }
        }
        return node;
    }

    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if (n == 1) {
            return {0};
        }
        vector<vector<int>> adj(n);
        for (auto & edge : edges) {
            adj[edge[0]].emplace_back(edge[1]);
            adj[edge[1]].emplace_back(edge[0]);
        }

        vector<int> parent(n, -1);
        /* 找到与节点 0 最远的节点 x */
        int x = findLongestNode(0, parent, adj);
        /* 找到与节点 x 最远的节点 y */
        int y = findLongestNode(x, parent, adj);
        /* 求出节点 x 到节点 y 的路径 */
        vector<int> path;
        parent[x] = -1;
        while (y != -1) {
            path.emplace_back(y);
            y = parent[y];
        }
        int m = path.size();
        if (m % 2 == 0) {
            return {path[m / 2 - 1], path[m / 2]};
        } else {
            return {path[m / 2]};
        }
    }
};


// ***
auto _{[]() noexcept {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);
  return 0;
}()};
class Solution {
private:
  static constexpr int N = 20010, M = 2 * N;
  int h[N], e[M], ne[M], idx;
  int deg[N];
  void add(int u, int v) { e[idx] = v, ne[idx] = h[u], h[u] = idx++; }

public:
  vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
    if (n == 1)
      return {0};
    if (n == 2)
      return {0, 1};
    memset(h, -1, sizeof h);
    for (auto& e : edges) {
      add(e[0], e[1]);
      add(e[1], e[0]); // an edge is bidirectional
      deg[e[0]]++;
      deg[e[1]]++;
    }
    queue<int> q;
    for (int i = 0; i < n; i++) {
      if (deg[i] == 1)
        q.emplace(i);
    }
    while (n > 2) {
      int s = q.size();
      n -= s;
      for (int i = 0; i < s; i++) {
        int u = q.front(); // a node with only one edge
        q.pop();
        for (int i = h[u]; ~i; i = ne[i]) { // traverse all the edges of the node
          int v = e[i];
          if (--deg[v] == 1)
            q.emplace(v);
        }
      }
    }
    vector<int> ans;
    while (!q.empty()) {
      ans.emplace_back(q.front());
      q.pop();
    }
    return ans;
  }
};