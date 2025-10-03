import argparse
import requests

def main():
    parser = argparse.ArgumentParser(description="Check a Github user's activity",add_help=True)
    parser.add_argument('username', type=str,help="Type in the Github username") 
    args = parser.parse_args()
    
    base_url = "https://api.github.com/users"

    # function to retrieve the users detail 
    def fetch_user_activity(name):
        if name != "":
            url = f"{base_url}/{name}/events"
            response = requests.get(url)

            if response.status_code == 200:
                #print("User detail successfully retrieved")
                user_data = response.json()
                return user_data 
            else: 
                print(f"Failed to retrieve {user_name} data: {response.status_code}")
        else:
            return 

    user_name = args.username       
    user_info = fetch_user_activity(user_name)

    if user_info:
        print(f"Here is {user_name} recent activity:\n")
        activities = {}
        for event in user_info:
            if event['type'] == 'PushEvent':
                repo_name =event['repo']['name']
                commit_count = event['payload']['size']
                if repo_name not in activities:
                    activities[repo_name] = commit_count
                else:
                    activities[repo_name] += commit_count
            elif event['type'] == 'IssuesEvent':
                print(f"* Created issue {event['payload']['issue']['number']}")
            elif event['type'] == 'WatchEvent':
                print(f"* Starred {event['repo']['name']}")
            elif event['type'] == 'IssueCommentEvent':
                print(f"* Commented on issue {event['payload']['issue']['number']}")
            elif event['type'] == 'CreateEvent':
                print(f"* Created {event['payload']['ref_type']} {event['payload']['ref']}")
            elif event['type'] == 'PullRequestEvent':
                print(f"* Created pull request {event['payload']['pull_request']['number']}")
            elif event['type'] == 'PullRequestReviewEvent':
                print(f"* Reviewed pull request {event['payload']['pull_request']['number']}")
            elif event['type'] == 'PullRequestReviewCommentEvent':
                print(f"* Commented on pull request {event['payload']['pull_request']['number']}")
            elif event['type'] == 'ForkEvent':
                print(f"* Forked {event['repo']['name']}")
            elif event['type'] == 'PublicEvent':
                print(f"* Made {event['repo']['name']} public")
            else:
                print(f"{event['type']}")
        # after getting all the push activities, then summarise the finding: 
        for repo_name, count in activities.items():
            if commit_count == 1: 
                word = "commit"
            else:
                word ="commits"
            print(f"* Pushed {count} {word} to {repo_name}\n")
    else:
        print("Invalid username")
if __name__ == "__main__":
    main()
