class Tract(object):
    def __init__(self, tractNo, pin, structureType, interest, contactStatus, name, streetAddress, mailingAddress, phoneNo, occupants, worksLand, contacted, attempts, consultationDate, followUp, comments, keepDelete, commodity, pipelineStatus):
        self.tractNo = tractNo
        self.pin = pin
        self.structureType = structureType
        self.interest = interest 
        self.contactStatus = contactStatus
        self.name = name
        self.streetAddress = streetAddress
        self.mailingAddress = mailingAddress
        self.phoneNo = phoneNo
        self.occupants = occupants
        self.worksLand = worksLand
        self.contacted = contacted
        self.attempts = attempts
        self.consultationDate = consultationDate
        self.followUp = followUp
        self.comments = comments
        self.keepDelete = keepDelete
        self.commodity = commodity
        self.pipelineStatus = pipelineStatus

# test = Tract(1, "112004345/NW-32-017-19-W2", 'BUSINESS/ UNKNOWN', 'RESIDENT OWNER', 'GREEN', 'ENBRIDGE PIPELINES INC', '', 'BOX 398 10201 JASPER AVENUE, EDMONTON, AB, T5J 2J9', 'HOME: 1-(204)-556-2632', '', '', '', '', '', '', 'MULTIPLE STRUCTURES', '', 'OIL', 'OPERATING')
