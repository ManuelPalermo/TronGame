import pygame
import random

class Cell:
	def __init__(self, pos, state):
		self.pos       = pos     # position of the cell
		self.state     = state   # state of the cell: ( empty \ str(number id of player who has passed on it))

class Player:
	def __init__(self, idd, name, pos):
		self.id        = idd     # number from 1 to 4
		self.name      = name    # name of the player
		self.pos       = pos     # current position of the player
		self.path      = []      # path taken so far by the player
		self.score     = 0       # score of the player
		self.last_move = "left"  # direction of the last move taken by player
		self.state     = "alive" # if player is dead or alive

	def move(self, move):
		'Computes the next move of a player'
		self.path.append([self.pos[0], self.pos[1]])
		if self.state=="alive":
			if   move == "last":   move = self.last_move
			if   move == "left":
				if self.last_move=="right" and self.score!=0:
					self.pos[0]+= 1
				else:
					self.pos[0]-= 1
					self.last_move="left"
			elif move == "right":
				if self.last_move == "left" and self.score!=0:
					self.pos[0]-= 1
				else:
					self.pos[0]+= 1
					self.last_move = "right"
			elif move == "up":
				if self.last_move == "down" and self.score!=0:
					self.pos[1]+= 1
				else:
					self.pos[1]-= 1
					self.last_move = "up"
			elif move == "down":
				if self.last_move == "up" and self.score!=0:
					self.pos[1]-= 1
				else:
					self.pos[1]+= 1
					self.last_move = "down"
			self.score    += 1


class TronEngine:
	def __init__(self, nplayers, size=(40, 25)):
		########## Game settings ########
		self.map_size   = size if size[0]>14 and size[1]>14 else (25, 15) # size must be at least (15, 15)
		########## Game Atributes #######
		self.map        = self.create_map()                               # array with cell objects
		self.players    = self.create_players(nplayers)                   # dict with player objects

	def play_music(self, music_file):
		try:
			pygame.mixer.init()
			pygame.mixer.music.load(music_file)
			pygame.mixer.music.play(-1, 0.0)
		except:
			print("Error playing music!")

	def wait4keypress(self, key=pygame.KEYDOWN):
		'Waits for a key to be pressed, else stays idle'
		while not pygame.event.peek(key):
			clock.tick(10)

	def create_map(self):
		'Initializes the map with cell objects'
		m = []
		for y in range(self.map_size[1]):
			m.append([Cell([x, y], "empty") for x in range(self.map_size[0])])
		return m

	def create_players(self, nplayers):
		'Initializes the dict with the players'
		starts_x = random.sample(range(5, self.map_size[0] - 5), nplayers)
		starts_y = random.sample(range(4, self.map_size[1] - 4), nplayers)
		players_pos = list(zip(starts_x, starts_y))
		players = {}
		for n in range(nplayers):
			name = "Broco " + str(n+1)#input("Insert player %s name: " % n)
			self.map[players_pos[n][1]][players_pos[n][0]].state = str(n)
			players[n] = Player(n, name, list(players_pos[n]))
		return players

	def reset_game(self):
		'Resets the game to an initial new random state'
		# reset cells
		for y in range(self.map_size[1]):
			for x in range(self.map_size[0]):
				self.map[y][x].state = "empty"
		#reset players
		starts_x = random.sample(range(5, self.map_size[0] - 5), len(self.players))
		starts_y = random.sample(range(4, self.map_size[1] - 4), len(self.players))
		for player in self.players.values():
			player.pos       = [starts_x[player.id], starts_y[player.id]]
			player.path      = []
			player.score     = 0
			player.last_move = "left"
			player.state     = "alive"
			self.map[player.pos[1]][player.pos[0]].state = player.id
		window.display_all(self.map)

	def player_moves(self):
		'Reads the input from the keyboard and makes palyers move'
		# https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed
		keys = pygame.key.get_pressed()
		if player_num > 0 and self.players[0].state=="alive": #player 1
			if   keys[pygame.K_LEFT]:      self.players[0].move("left")
			elif keys[pygame.K_RIGHT]:     self.players[0].move("right")
			elif keys[pygame.K_UP]:        self.players[0].move("up")
			elif keys[pygame.K_DOWN]:      self.players[0].move("down")
			else:                          self.players[0].move("last")
		if player_num > 1 and self.players[1].state=="alive": #player 2
			if   keys[pygame.K_a]:         self.players[1].move("left")
			elif keys[pygame.K_d]:         self.players[1].move("right")
			elif keys[pygame.K_w]:         self.players[1].move("up")
			elif keys[pygame.K_s]:         self.players[1].move("down")
			else:                          self.players[1].move("last")
		if player_num > 2 and self.players[2].state=="alive": #player 3
			if   keys[pygame.K_j]:         self.players[2].move("left")
			elif keys[pygame.K_l]:         self.players[2].move("right")
			elif keys[pygame.K_i]:         self.players[2].move("up")
			elif keys[pygame.K_k]:         self.players[2].move("down")
			else:                          self.players[2].move("last")
		if player_num > 3 and self.players[3].state=="alive": #player 4
			if   keys[pygame.K_KP4]:       self.players[3].move("left")
			elif keys[pygame.K_KP6]:       self.players[3].move("right")
			elif keys[pygame.K_KP8]:       self.players[3].move("up")
			elif keys[pygame.K_KP5]:       self.players[3].move("down")
			else:                          self.players[3].move("last")
		if player_num > 4 and self.players[4].state=="alive": #player5
			if   keys[pygame.K_f]:         self.players[4].move("left")
			elif keys[pygame.K_h]:         self.players[4].move("right")
			elif keys[pygame.K_t]:         self.players[4].move("up")
			elif keys[pygame.K_g]:         self.players[4].move("down")
			else:                          self.players[4].move("last")

	def check_invalid(self):
		'Checks if a player´s posiion is invalid and if so, removes it from the game'
		invalid  = []
		for player in [p for p in self.players.values() if p.state=="alive"]:
			invalid += player.path
		l2remove = []
		for player in [p for p in self.players.values() if p.state=="alive"]:
			if   ( player.pos[0]==-1 or player.pos[0]==eng.map_size[0]
				or player.pos[1]==-1 or player.pos[1]==eng.map_size[1]
				or player.pos in invalid
				or player.pos in [p.pos for p in self.players.values() if p.id!=player.id]):
				l2remove.append(player)
			else:
				cell = eng.map[player.pos[1]][player.pos[0]]
				cell.state = str(player.id)
				window.display_cell(cell)
		self.remove_player(l2remove)

	def remove_player(self, players2remove):
		'Removes the player from the game, making the necessary changes'
		for player in players2remove:
			player.state = "dead"
			while player.path:
				pos = player.path.pop()
				cell = self.map[pos[1]][pos[0]]
				cell.state = "empty"
				window.display_cell(cell)

	def check_winner(self):
		'Checks a player has won(if its the only one still alive)'
		players_alive = [p for p in self.players.values() if p.state=="alive"]
		if len(players_alive)<=1:
			scored_players = [[p, p.score] for p in self.players.values() if p.state=="dead"]
			scored_players.sort(key=lambda x: x[1])
			scored_players += [[p, p.score] for p in self.players.values() if p.state=="alive"]
			window.display_ending_score(scored_players[::-1])
			return True

class TronWindow:
	def __init__(self, map_size, cell_size):
		################ Window size #######################
		self.map_size  = map_size if map_size[0]>14 and map_size[1]>14 else (25, 15)  # size of the window (in cells)
		self.csize     = cell_size                                                    # size of each cell (in pixels)
		self.win_size  = (self.map_size[0]*cell_size, self.map_size[1]*cell_size)     # size of the window (in pixels)
		################ Pygame Window #####################
		pygame.init()
		self.window    = pygame.display.set_mode(self.win_size)           # game window using pygame
		pygame.display.set_caption('Tron Game')                           # name of the window
		self.display_rules_controls()

	def update(self):
		'Calls pygame´s display.flip(), updating the screen with drawn objects(pygame uses double buffer)'
		pygame.display.flip()

	def display_all(self, mapp):
		'Displays all the cells in the screen (used to initialize the game screen)'
		self.window.fill(((10, 10, 10)))
		for y in range(self.map_size[1]):
			pygame.draw.line(self.window, (75, 75, 75), [0, y*cell_size],[self.win_size[0], y*cell_size])
			for x in range(self.map_size[0]):
				pygame.draw.line(self.window, (75, 75, 75), [x*cell_size, 0], [x*cell_size, self.win_size[1]])
				if mapp[y][x].state!="empty":
					self.display_cell(mapp[y][x])
		self.update()

	def display_cell(self, cell):
		' Displays the cell on the board'
		# player colors 1->red /  2->Green  /  3->Blue  /  4-> Yellow  /  5-> Pink
		color = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
		draw_posx , draw_posy  =  cell.pos[0]*self.csize,    cell.pos[1]*self.csize
		if cell.state=="empty":
			pygame.draw.rect(self.window, (10, 10, 10), (draw_posx+1, draw_posy+1, self.csize-1, self.csize-1))
		else:
			pygame.draw.rect(self.window, color[int(cell.state)], (draw_posx+1, draw_posy+1, self.csize-1, self.csize-1))

	def display_ending_score(self, scored_players):
		'Displays the score of the players after a player has won'
		self.window.fill(((10, 10, 10)))
		for place, [player, score] in enumerate(scored_players):
			if place==0: score="Won!"
			font_size  = 50 - 5 * (place+1)
			myfont     = pygame.font.SysFont("monospace", font_size)
			st2display = "%sº - %s  (%s)" % (str(place + 1), player.name, str(score))
			pos        = [(self.win_size[0]-font_size*len(st2display)/1.7)/2, self.win_size[1]*((place+1)/(len(scored_players)+2))]
			label      = myfont.render(st2display, True, (255, 255, 255))
			self.window.blit(label, pos)
		self.update()

	def display_rules_controls(self):
		'Displays the rules and commands of the game in the window'
		picture  = pygame.image.load("TronGameCover.png")
		picture  = pygame.transform.scale(picture, (self.win_size[0]-2, int(self.win_size[1])-2))
		pict_pos = picture.get_rect().move((1,1))
		self.window.blit(picture, pict_pos)
		self.update()


if __name__ == '__main__':
	player_num = 2          # from 1 to 5 players
	game_size  = (40, 25)   # game size in cells           -> (game window in pixles games size*cell_size)
	cell_size  = 20         # size of each cell in pixels  -> (should be at least 600x300 for a good display)
	game_speed = 15         # fps = moves per second       -> recommended 10-15
	clock      = pygame.time.Clock()
	eng        = TronEngine(player_num, game_size)
	eng.play_music("sandstorm_darude.mp3")
	window     = TronWindow(game_size, cell_size)
	eng.wait4keypress()
	window.display_all(eng.map)
	clock.tick(0.8)
	running = True
	while running:
		clock.tick(game_speed)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		eng.player_moves()
		eng.check_invalid()
		if eng.check_winner()==True:
			eng.wait4keypress()
			eng.reset_game()
			clock.tick(0.8)
		window.update()
