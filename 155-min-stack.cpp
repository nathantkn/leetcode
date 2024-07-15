class MinStack {
private:
    stack<int> stack;
    ::stack<int> min;
public:    
    void push(int val) {
        stack.push(val);
        if (min.empty() || val < min.top()) {
            min.push(val);
        } else {
            min.push(min.top());
        }
    }
    
    void pop() {
        stack.pop();
        min.pop();
    }
    
    int top() {
        return stack.top();
    }
    
    int getMin() {
        return min.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
