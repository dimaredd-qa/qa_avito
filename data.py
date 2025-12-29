main_url = "https://qa-internship.avito.com/"

class Endpoint:
    create_ad_url = f"{main_url}api/1/item"
    get_ad_by_id = f"{main_url}api/1/item/{{ad_id}}"
    del_ad_by_id = f"{main_url}api/2/item/{{del_id}}"
    get_ads_by_seller_id = f"{main_url}api/1/{{seller_id}}/item"
    get_statistic_v1 = f"{main_url}api/1/statistic/{{stat_id}}"
    get_statistic_v2 = f"{main_url}api/2/statistic/{{stat_id}}"

class ZeroInField:
    field = [
        ("price", "ТС003"),
        ("likes", "ТС004"),
        ("viewCount", "ТС005"),
        ("contacts", "ТС006"),
    ]

class MissingField:
    field =[
        ("sellerID", "ТС007"),
        ("name", "ТС015"),
        ("price", "ТС021"),
        ("statistics", "ТС049")
    ]

class MissingFieldStatistics:
    field = [
        ("likes", "ТС028"),
        ("viewCount", "ТС035"),
        ("contacts", "ТС042")
    ]
class InvalidField:
    invalid_fields = [
        ("sellerID", "331155", "ТС008"),
        ("sellerID", None, "ТС009"),
        ("sellerID", 0, "ТС010"),
        ("sellerID", 331155.1, "ТС011"),
        ("sellerID", -331155, "ТС012"),
        ("sellerID", 3000000, "ТС013"),
        ("sellerID", True, "ТС014"),
        ("name", 331155, "ТС018"),
        ("name", None, "ТС016"),
        ("name", "", "ТС017"),
        ("name", [], "ТС020"),
        ("name", True, "ТС019"),
        ("price", "331155", "ТС022"),
        ("price", None, "ТС023"),
        ("price", 331155.1, "ТС024"),
        ("price", -331155, "ТС025"),
        ("price", 3000000, "ТС026"),
        ("price", True, "ТС027"),
        ("statistics", None, "ТС050"),
        ("statistics", {}, "ТС051"),
        ("statistics", [], "ТС052"),
        ("statistics", "", "ТС053")
    ]

    statistics_fields = [
        ("likes", "331155", "ТС029"),
        ("likes", None, "ТС030"),
        ("likes", 331155.1, "ТС031"),
        ("likes", -331155, "ТС032"),
        ("likes", 3000000, "ТС033"),
        ("likes", True, "ТС034"),
        ("viewCount", "331155", "ТС036"),
        ("viewCount", None, "ТС037"),
        ("viewCount", 331155.1, "ТС038"),
        ("viewCount", -331155, "ТС039"),
        ("viewCount", 3000000, "ТС040"),
        ("viewCount", True, "ТС041"),
        ("contacts", "331155", "ТС043"),
        ("contacts", None, "ТС044"),
        ("contacts", 331155.1, "ТС045"),
        ("contacts", -331155, "ТС046"),
        ("contacts", 3000000, "ТС047"),
        ("contacts", True, "ТС048"),
    ]

    invalid_get_ad_by_id = [
        ("97928230-9999-9999-9999-717ecd42aaf3", "TC056"),
        ("getid", "TC057"),
        ("123' OR '1'='1", "TC058"),
        ("", "TC059")
    ]

    invalid_seller_id_for_get = [
        (10*"999999999999717", "TC066"),
        ("getid", "TC066.1"),
        ("123' OR '1'='1", "TC066.2"),
        ("", "TC067")
    ]