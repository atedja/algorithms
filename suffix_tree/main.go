package main

import (
	"fmt"
)

type node struct {
	index int
	edges map[string]*node
}

func newNode(i int) *node {
	n := &node{
		index: i,
		edges: make(map[string]*node),
	}
	return n
}

// Given two strings a and b, returns the index where a and b differ
// Index returned cannot be greater than the shorter string
func findSplitIndex(a string, b string) int {
	i := 0
	for ; i < len(a) && i < len(b); i++ {
		if a[i] != b[i] {
			return i
		}
	}
	return i
}

func generateSuffixTree(input string) *node {
	root := newNode(-1)
	for i := 0; i < len(input); i++ {
		lookup := input[i:]
		current := root
		for current != nil {
			if lookup == "" {
				current.edges[""] = newNode(i)
				break
			}

			found := false
			for k, v := range current.edges {
				// look for the edge that begins with the same key we are looking up
				si := findSplitIndex(k, lookup)
				if si == 0 {
					continue
				}

				found = true
				delete(root.edges, k)
				inode := newNode(-1)
				root.edges[k[:si]] = inode
				inode.edges[k[si:]] = v
				current = inode
				lookup = lookup[si:]
				break
			}

			if !found {
				// no key is found, insert a new one
				current.edges[lookup] = newNode(i)
				break
			}
		}
	}
	return root
}

func printSuffixTree(n *node, level int) {
	if n == nil {
		return
	}

	if len(n.edges) == 0 {
		printTabs(level)
		fmt.Printf("{%d}\n", n.index)
		return
	}

	for k, v := range n.edges {
		if k == "" {
			k = "$"
		}
		printTabs(level)
		fmt.Printf("%s\\\n", k)
		printSuffixTree(v, level+1)
	}
}

func printTabs(n int) {
	for i := 0; i < n; i++ {
		fmt.Printf("\t")
	}
}

func main() {
	root := generateSuffixTree("geeksforgeeks")
	printSuffixTree(root, 0)
}
