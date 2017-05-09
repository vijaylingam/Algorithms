import java.io.*;
import java.lang.Integer;

class Node{
    public int key;//This denotes the key stored at the node
    public String value;//This denotes the value stored in the node.
    public Node leftChild;//This is a reference to the left child in the binary tree
    public Node rightChild;//This is a reference to the right child in the binary tree
    public Node parent;//This is a reference to the parent of the node in the binary tree.
    
    public Node(){
        parent = leftChild = rightChild = null;
    }
}

public class BinarySearchTree{
    public Node root;
    public int size;
    
    //This is the initialization method for Binary Search Tree.
    public BinarySearchTree(){
        size = 0;
        root = null;
    }
    
    //This method checks if the given node is a leaf
    public boolean isLeaf(Node N){
        if(N.leftChild == null && N.rightChild == null)return(true);
        else return(false);
    }
    
    
    //This method implements the get method discussed in class.
    public String get(int k) throws NullPointerException{
        //To be written as part of Homework
        Node p = root;
        while(p!=null){
            if(p.key == k){
                return p.value;
            }
            if(k < p.key){
                p = p.leftChild;
            }
            if(p != null) {
                if (k > p.key) {
                    p = p.rightChild;
                }
            }
        }
        return "does not exist";
    }
    
    
    //This method implements the put method discussed in class.
    public String put(int k, String v){
        //To be written as part of Homework
        Node N = new Node();
        N.key = k;
        N.value = v;
        String str = "";
        if(size == 0){
            root = N;
            size ++;
            return root.value;
        }
        if(root.key == k){ //change the value of root Node if the key already exists
            str = root.value;
            root.value = v;
            return str;
        }
        Node current = root;
        Node parent;
            while(true){
                parent = current;
                if(k<current.key){
                    current = current.leftChild;
                    if(current==null){
                        parent.leftChild = N;
                        N.parent = parent;
                        size++;
                        return N.value;
                    }
                    if(current.key == k){ //change the value if the key already exists
                        str = current.value;
                        current.value = v;
                        return str;
                    }
                }else{
                    current = current.rightChild;
                    if(current==null){
                        parent.rightChild = N;
                        N.parent = parent;
                        size++;
                        return N.value;
                    }
                    if(current.key == k){ //change the value if the key already exists
                        str = current.value;
                        current.value = v;
                        return str;
                    }
                }
            }
    }        
    
    //This method implements the remove method discussed in class
    public void remove(int k) throws NullPointerException{
        //To be written as part of Homework.
        if(get(k) == "does not exist")return;
        else{
            Node p = root;
            while(p!=null){
                if(p.key == k){
                    if(isLeaf(p)){  //Remove a Leaf Node
                        Node N = new Node();
                        if(p.key < p.parent.key) {
                            p.parent.leftChild = N;
                            size--;
                            return;
                        }
                        if(p.key > p.parent.key) {
                            p.parent.rightChild = N;
                            size--;
                            return;
                        }
                    }
                    if(p.rightChild == null){
                        if(p.parent.leftChild.key == k){ p.parent.leftChild = p.leftChild; size--; return; }
                        if(p.parent.rightChild.key == k) p.parent.rightChild = p.leftChild;
                        size--;
                        return;
                    }
                    if(p.leftChild == null){
                        if(k < p.parent.key){
                            p.parent.leftChild = p.rightChild;
                            size--;
                            return;
                        }
                        else{
                            p.parent.rightChild = p.rightChild;
                            size--;
                            return;
                        }
                    }
                    else{
                        Node q = p;
                        q = q.leftChild;
                        while(q.rightChild != null)q=q.rightChild;
                        if(p.parent == null)root = q;
                        else{
                            if(k < p.parent.key) {p.parent.leftChild.value = q.value; p.parent.leftChild.key = q.key; }
                            else{p.parent.rightChild.value = q.value; p.parent.rightChild.key = q.key;  }
                        }
                        if(q.key < q.parent.key){
                            q.parent.leftChild = q.leftChild;
                            size--;
                            return;
                        }
                        else{
                            q.parent.rightChild = q.leftChild;
                            size --;
                            return;
                        }
                       //System.out.println(q.leftChild.key);
                    }
                }
                if(k < p.key){
                    p = p.leftChild;
                }
                if(k > p.key){
                    p = p.rightChild;
                }
            }
        }
    }
}