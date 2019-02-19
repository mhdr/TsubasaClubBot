from db.users import Users


class Commands:

    def __init__(self):
        pass

    @staticmethod
    def share(chatId):
        users = Users()
        users.update_status(chatId, 1)
        return Commands.status()

    @staticmethod
    def join(chatId):
        users = Users()
        users.update_status(chatId, 2)
        return Commands.status()

    @staticmethod
    def end(chatId):
        users = Users()
        users.update_status(chatId, 3)
        return Commands.status()

    @staticmethod
    def request_join(chatId):
        users = Users()
        matches = users.findBy_chatId(chatId)
        username = matches["username"]
        output = "@{username} : Request Join".format(username=username)
        return output

    @staticmethod
    def request_share(chatId):
        users = Users()
        matches = users.findBy_chatId(chatId)
        username = matches["username"]
        output = "@{username} : Request Share".format(username=username)
        return output

    @staticmethod
    def status():
        users = Users()

        users_share = users.find_start_share()
        users_join = users.find_start_join()

        users_share_output = ""
        users_join_output = ""

        for s in users_share:
            username = s["username"]
            users_share_output += "@{username}\n\r".format(username=username)

        for j in users_join:
            username = j["username"]
            users_join_output += "@{username}\n\r".format(username=username)

        count_share = users_share.count()
        count_join = users_join.count()

        output = "Share : {share}\n\r" \
                 "{users_share}" \
                 "Join : {join}\n\r" \
                 "{users_join}".format(share=count_share,
                                       join=count_join,
                                       users_share=users_share_output,
                                       users_join=users_join_output)

        return output
