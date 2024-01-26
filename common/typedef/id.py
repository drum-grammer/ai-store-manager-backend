class ID(str):
    def __str__(self):
        return super().__str__()


class UserID(ID):
    pass


class TemplateID(ID):
    pass


class InspectionItemID(ID):
    pass


class ReportID(ID):
    pass


class InspectionItemLogID(ID):
    pass
