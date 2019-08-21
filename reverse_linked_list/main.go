package main

import "fmt"

type node struct {
	v    rune
	next *node
}

func genNodes(str string) *node {
	head := &node{rune(str[0]), nil}
	prev := head
	for i := 1; i < len(str); i++ {
		n := &node{rune(str[i]), nil}
		prev.next = n
		prev = n
	}
	return head
}

func printNodes(n *node) {
	for n != nil {
		fmt.Printf("%c", n.v)
		n = n.next
	}
	fmt.Println()
}

func reverseNode(n *node) *node {
	if n == nil || n.next == nil {
		return n
	}

	o := n.next
	n.next = nil
	for o != nil {
		nx := o.next
		o.next = n
		n, o = o, nx
	}

	return n
}

func main() {
	head := genNodes("hello world")
	printNodes(head)
	head = reverseNode(head)
	printNodes(head)
}
