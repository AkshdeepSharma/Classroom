class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_list = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            local_name = "".join(local_name.split('+')[0].split('.'))
            email = local_name + "@" + domain_name
            email_list.add(email)
        return len(email_list)