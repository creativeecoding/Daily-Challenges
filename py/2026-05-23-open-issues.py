"""
Challenge: Open Issues
Description: Given an array of issue numbers and another array of pull request (PR) numbers, return an array of issues that remain open after all PRs have been merged.
A PR closes an issue if their digits are a rotation of each other. For example, issue 123 would be closed by PR 231 or 312.
A PR does not close an issue with the exact same number. For example, PR 123 does not close issue 123. So an issue with all the same number can't get closed.
Either number may have leading zeros stripped. For example, PR 201 would close issue 12 (012, a rotation of 201). Similarly, issue 201 would be closed by PR 12.
Return the remaining open issues in the order they were given.
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
