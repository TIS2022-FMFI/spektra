from PySide6.QtWidgets import QTreeView

def show_context_menu(self, point):
    index = self.indexAt(point)
    if index.isValid():
        self.context_menu.exec_(self.mapToGlobal(point))


def setup_filemanager_view(tree_view: QTreeView):
    tree_view.setRootIsDecorated(False)
    tree_view.setAlternatingRowColors(True)
    tree_view.setSortingEnabled(True)
    tree_view.setAnimated(True)
    tree_view.setUniformRowHeights(True)
    tree_view.setDragEnabled(True)
    tree_view.setAcceptDrops(False)
    tree_view.setDropIndicatorShown(True)
    tree_view.setWordWrap(True)
    tree_view.header().setStretchLastSection(True)
    tree_view.setAutoScroll(True)
