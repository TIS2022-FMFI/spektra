from PySide6.QtWidgets import QTreeView


def setup_filemanager_view(tree_view: QTreeView):
    """
    Setup file manager view.
    @param tree_view: QTreeView instance to set up.
    """
    tree_view.setRootIsDecorated(False)
    tree_view.setAlternatingRowColors(False)
    tree_view.setSortingEnabled(True)
    tree_view.setAnimated(True)
    tree_view.setUniformRowHeights(True)
    tree_view.setDragEnabled(True)
    tree_view.setAcceptDrops(False)
    tree_view.setDropIndicatorShown(True)
    tree_view.setWordWrap(True)
    tree_view.header().setStretchLastSection(True)
    tree_view.setAutoScroll(True)
