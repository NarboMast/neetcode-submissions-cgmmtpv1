class MinStack {
    private record Pair(
        int val,
        int min
    ){}

    //{-2, -2}, {0, -2}

    private final Stack<Pair> stack;

    public MinStack() {
        stack = new Stack<>();
    }
    
    public void push(int val) {
        if(stack.empty() || val < stack.peek().min){
            stack.push(new Pair(val, val));
        } else {
            stack.push(new Pair(val, stack.peek().min));
        }
    }
    
    public void pop() {
        stack.pop();
    }
    
    public int top() {
        return stack.peek().val;
    }
    
    public int getMin() {
        return stack.peek().min;
    }
}
