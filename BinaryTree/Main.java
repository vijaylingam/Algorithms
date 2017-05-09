public class Main{
    public static void main(String args[]){
        BinaryTree B = new BinaryTree();
        System.out.println("Pre Order Traversal:");
        B.preOrderTraversal(B.root);

        System.out.println("Post Order Traversal:");
        B.postOrderTraversal(B.root);

        System.out.println("In Order Traversal:");
        B.inOrderTraversal(B.root);
        
        //B.addLeft(B.root, 17);
        //B.addRight(B.root, 18);
        System.out.println("The height of the given tree is:" + B.computeHeight(B.root));
        System.out.println("The depth of the given tree is:" + B.computeDepth(B.root));
        System.out.println("Number of nodes in the given tree is:" + B.computeSize(B.root));
    }
}