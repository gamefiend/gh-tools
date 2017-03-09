from github import Github
from env import GITHUB_TOKEN, DEFAULT_ORG, USER
from gh_format import * 
from readchar import readkey

g = Github(GITHUB_TOKEN)

def gh_init(gh):
	return g.get_organization(DEFAULT_ORG)
		
def get_issues(option,gh):
	return gh.get_issues(filter=option,state='open')

def display_issues(issues):
    display = PrettyTable(["Title", "Link", "Description"])
    for i in issues:
        display.add_row([print_display(i.title),print_url(i.url),i.body[:30]])
    print display

def show_filter(filter):
	clear()
	print "\n\n\n"
	print print_title("{} Issues".format(filter))
	issues = get_issues(filter,org)
	display_issues(issues) 
	print print_msg("a -- assigned issues | m -- mentioned Issues | c -- created issues | s -- subscribed | q -- quit")

if __name__ == "__main__":
	org = gh_init(g)
	show_filter('assigned')
	while(1):
		kp = readkey()
		if kp == 'q':
			break
		elif kp == 'a':
			show_filter('assigned')
		elif kp == 'm':
			show_filter('mentioned')
		elif kp == 'c':
			show_filter('created')
		elif kp == 's':
			show_filter('subscribed')
		else:
			print('Unknown Input --- press a key to continue')
			cont = readkey()
			show_filter('assigned')
			

    
