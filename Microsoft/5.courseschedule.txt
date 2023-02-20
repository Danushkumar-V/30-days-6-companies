class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] indegree = new int[numCourses];
        Queue<Integer> q = new LinkedList<>();
        int count = 0;
        
        //convert pre-req to adj list
        ArrayList<ArrayList<Integer>> adjList = new ArrayList<>();
        for(int i = 0; i < numCourses; i++) {
            adjList.add(new ArrayList<>());
        } 

        for(int i = 0; i < prerequisites.length; i++) {
            adjList.get(prerequisites[i][0]).add(prerequisites[i][1]);
        }

        //count the indegree for node/task
        for(int i = 0; i < numCourses; i++) {
            for(int adj : adjList.get(i)) {
                indegree[adj]++;
            }
        }

        //try to do the topo sort, its done for n elements, then true, else there is a          cycle so false
        for(int i = 0; i < numCourses; i++) {
            if(indegree[i] == 0) q.add(i);
        }

        while(!q.isEmpty()) {
            int node = q.poll();
            count++;
            for(int adj : adjList.get(node)) {
                indegree[adj]--;
                if(indegree[adj] == 0) {
                    q.add(adj);
                }
            }
        }
        if(count == numCourses) 
            return true;
        else
            return false;
    }
}
