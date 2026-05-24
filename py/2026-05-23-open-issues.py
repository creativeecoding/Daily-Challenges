"""
Challenge: Open Issues
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-23
"""

def get_open_issues(issues, prs):
    open_issues = []
    
    for issue in issues:
        for pr in prs:
            if issue == pr:
                continue
                
            i_str = str(issue)
            p_str = str(pr)
            
            length = max(len(i_str), len(p_str))
            i_pad = i_str.zfill(length)
            p_pad = p_str.zfill(length)
            
            if p_pad in (i_pad * 2):
                break
        else:
            open_issues.append(issue)
            
    return open_issues
