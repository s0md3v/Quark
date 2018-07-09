# Quark
Quark is a data visualization framework.

![Quark Logo](https://image.ibb.co/evD5cT/Screenshot_2018_07_08_00_58_59_small.png)

## Introduction
**Quark** is framework built on top of [Linkurious.js](https://github.com/Linkurious/linkurious.js) which lets you painlessly visualize your data in form of nodes & edges. It offers a lot of features out of the box and runs in a browser so you don't need to worry about installing anything or configuring things. Just feed it some data and Quark will plot a beautiful and intractable graph out of it.\
Here's a screenshot if you are eager to take a look at it:

![Quark UI](https://image.ibb.co/ftrKp8/Screenshot_2018_07_09_19_19_11.png)

### Browser Support
All modern web browsers are supported, including:

- Internet Explorer 10+
- Chrome 23+ and Chromium
- Firefox 15+
- Safari 6+

Touch events on tablet and mobile are currently supported as beta features.

### Usage

#### In-Graph Controls
- `left click` Select a node
- `right click` Highlight edges of the node
- `drag` Move around
- `mousewheel` zoom in & zoom out

#### Keyboard Controls
- `Keyboard Arrows` Move around
- `spacebar + +` Zoom in
- `spacebar + -` Zoom out
- `spacebar + a` Select/deselect all nodes
- `spacebar + e` Select neighbors of selected node(s)
- `spacebar + u` Deselect nodes
- `spacebar + i` Select nodes with no edges
- `spacebar + l` Select nodes with 1 edge

#### Features
Options in the sidebar are divided in sections and their documentation here follows the same style.

##### Circle
It arranges the nodes in a circular layout.

![Circle demo](https://preview.ibb.co/erc0e8/Screenshot_2018_07_09_13_50_03.png)

##### Center
Click a node and then click on the center option to place it in the center of the graph.

##### Decolor
It resets the color of all edges and nodes.

##### Lasso
Lasso tool lets you select nodes by drawing a line around them.

![Lasso demo](https://preview.ibb.co/cEVLe8/Screenshot_2018_07_09_13_53_24.png)

##### Stabilize
It optimizes the size of nodes that are too small or too big.

##### Clean
It removes nodes & edges which are too small.

##### Delete
It deletes the selected node(s) from the graph.

------
##### Edge Style (Dropdown)
The dropdown list lets you select different types of edge styles.\
Supported edge styles are:
- `line` Simple straight lines
- `Curved` Curved lines
- `Arrow` Arrows that point towards the target of the edge
- `cArrows` Arrows but curved

![Edge style demo](https://preview.ibb.co/it7iGo/FotoJet.jpg)

##### Edges {int}
It shows the total number of edges. You can click it to toggle edges on/off.

##### Nodes {int}
It shows the total number of nodes. You can click it to toggle nodes on/off.

##### Edge labels
Toggle edge labels on/off.

##### Node labels
Toggle node labels on/off.

##### Color
The color option lets you choose a color from a color picker and apply it to the selected node(s).

##### Find
Enter full label/id of a node and it will find and highlight it. Default color is `yellow`.

------

##### Make/Color Clusters
It helps you fine & color nodes that are more densely connected together than to the rest of the network.
![Cluster demo](https://preview.ibb.co/fXPfwo/Screenshot_2018_07_09_14_36_21.png)

##### Level (Dropdown)
It lets you select the "aggressiveness" to use while coloring the communities. Lower the level, higher the number of communities.

##### Reset
It simply resets the color change made by the cluster option. However it doesn't reset the the position of the nodes i.e. they remain in cluster form.


#### How to load a graph?
##### Scenario 1
You have 5 points `a, b, c, d, e` and you know the relationships between them like `a` is related to `c`.
Then create a file with the contents
```
a,e
c,d
e,a
d,e
a,c
c,e
```
Save it with any name and any extension and feed it to `quark.py` as follows
`python3 quark.py <filename>`
That's it! Open `quark.html` and you will see your graph.

###### Result
![case 1](https://preview.ibb.co/e4TACT/Screenshot_2018_07_09_19_50_31.png)

Why are the nodes so small? Because in this *automatic mode*, the size of a node is determined by how many other nodes are connected to. For any noticeable variation in node size, your graph should have enough nodes i.e. larger than 20.

##### Scenario 2
If you are like me and you want full control of everything like the co-ordinates and size of nodes, edge thickness and their labels etc. then you will need to arrange this information in JSON syntax as follows:
```
{
"nodes": [{"label": "a", "x": 1, "y": 1, "id": "node1", "size":10}, {"label": "b", "x": 2, "y": 1, "id": "node2", "size":4}],
"edges": [{"source":"node1", "target":"node2", "id":"edge1", "size":2}]
}
```
Save it with any name and again, pass it to the handler and open quark.html

###### Result

![case 2](https://image.ibb.co/cEUYXT/Screenshot_2018_07_09_19_46_35.png)

### Performance
Quark is tested and built on a spaghetti laptop with just 3GB RAM, built-in graphic card & i3 processor. On this configuration, a graph with 7000 nodes & 3000 edges was rendering just fine.\
A computer with better specifications will be able to handle more data smoothly. Just to be on the safe side, Quark prompts the user for using `webgl` renderer if the number of edges is more than 8000.\
`webgl` uses your GPU to render graphs which boosts the performance but it doesn't support interaction events.
Quark uses `canvas` renderer by default.

Tips:
- Edges consume more memory than nodes.
- Memory caused by edge styles: `line < curve < arrow < curved arrow`
- Delete the nodes which seem insignificant to you.
- Hide edges/nodes when you are not dealing with them.
- Hide node labels (you will still be able to see them on hovering over nodes).
- Hide edge labels.

### Contribution
Quark is built on top of [Linkurious.js](https://github.com/Linkurious/linkurious.js) and the files from Linkurious.js are stored in the `libs` directory. The bugs in them are out of scope so don't open an issue here. You are welcome if you want to fix issues yourself with a pull request./
Feel free to open issues about a bug, question or feature request.
