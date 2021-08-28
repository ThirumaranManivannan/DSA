def tournamentWinner(competitions, results):
	points = {}
	max_point = 0
	winner = ""
	for idx in range(len(results)):
		match_res = results[idx]
		compete_teams = competitions[idx]
		if match_res == 1:
			team_won = compete_teams[0]
			if team_won in points:
				val = points[team_won]
				points[team_won] = val + 3
			else:
				points[team_won] = 3
		else:
			team_won = compete_teams[1]
			if team_won in points:
				points[team_won] = points[team_won] + 3
			else:
				points[team_won] = 3
	for team, point in points.items():
		if max_point < point:
			max_point = point
			winner = team
	return winner


competitions = [
	["HTML", "Java"],
	["Java", "Python"],
	["Python", "HTML"]
]
results = [0, 1, 1]

print(tournamentWinner(competitions, results))
