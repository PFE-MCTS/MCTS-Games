import sys

import chess
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget

import database
from Node import *
from chessGame import *
from TPlayer import *
from MCTS import *
from database import *

class MainWindow(QWidget):
    """
    Create a surface for the chessboard.
    """

    jeu = chessGame()
    currentGameState = {'board': deepcopy(jeu.board), 'nextPlayer': "WHITE", 'value': None}
    player1 = Tplayer()
    mcts = Mcts(jeu, 1)
    mcts.CurrentGameNode = mcts.initialize(jeu, currentGameState, "chess")  # créer la racine et les fils de la racine
    lastMCTSState = currentGameState

    def __init__(self):
        """
        Initialize the chessboard.
        """
        super().__init__()

        self.setWindowTitle("Jeu d'echecs Master 2 ADSI")
        self.setGeometry(300, 300, 650, 650)

        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(10, 10, 600, 600)

        self.boardSize = min(self.widgetSvg.width(),
                             self.widgetSvg.height())
        self.coordinates = True
        self.margin = 0.05 * self.boardSize if self.coordinates else 0
        self.squareSize = (self.boardSize - 2 * self.margin) / 8.0
        self.pieceToMove = [None, None]
        self.board = chess.Board()
                                                                        # initilisation du jeu avec MCTS


        self.drawBoard()

    @pyqtSlot(QWidget)
    def mousePressEvent(self, event):
        """
        Handle left mouse clicks and enable moving chess pieces by
        clicking on a chess piece and then the target square.

        Moves must be made according to the rules of chess because
        illegal moves are suppressed.
        """
        if event.x() <= self.boardSize and event.y() <= self.boardSize:
            if event.buttons() == Qt.LeftButton:
                if self.margin < event.x() < self.boardSize - self.margin and self.margin < event.y() < self.boardSize - self.margin:
                    file = int((event.x() - self.margin) / self.squareSize)
                    rank = 7 - int((event.y() - self.margin) / self.squareSize)
                    square = chess.square(file, rank)
                    piece = self.board.piece_at(square)
                    coordinates = "{}{}".format(chr(file + 97), str(rank + 1))
                    change =False
                    if self.pieceToMove[0] is not None:
                        move = chess.Move.from_uci("{}{}".format(self.pieceToMove[1], coordinates))
                        if move in self.board.legal_moves:
                            self.board.push(move)
                            change = True
                            # joueur 1

                            MainWindow.currentGameState = MainWindow.player1.Playerinterface(MainWindow.jeu, MainWindow.currentGameState, move)
                            board = deepcopy(MainWindow.currentGameState['board'])
                            self.board = deepcopy(board)
                            self.drawBoard()


                        piece = None
                        coordinates = None
                    self.pieceToMove = [piece, coordinates]
                    self.drawBoard()


                    self.computerPlay(change)
                    self.drawBoard()
                    print("this is the last line")

    def computerPlay(self, change):
        if change == True:
            # ici demander a l'ordinateur de jouer .
            MainWindow.currentGameState = MainWindow.mcts.ComputerPlay(MainWindow.jeu,
                                                                       MainWindow.currentGameState,
                                                                       MainWindow.mcts.CurrentGameNode)
            MainWindow.lastMCTSState = deepcopy(MainWindow.currentGameState)
            board = deepcopy(MainWindow.currentGameState['board'])
            self.board = deepcopy(board)
            return self.board

        print("computer play\n")

    def drawBoard(self):
        """
        Draw a chessboard with the starting position and then redraw
        it for every new move.
        """
        self.boardSvg = self.board._repr_svg_().encode("UTF-8")
        self.drawBoardSvg = self.widgetSvg.load(self.boardSvg)
        return self.drawBoardSvg






if __name__ == "__main__":
    chessGui = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(chessGui.exec_())