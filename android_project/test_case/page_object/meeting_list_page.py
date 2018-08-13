#coding:utf-8
from paperless_project.android_project.test_case.page_object.base import Base


class MeetingListPage(Base):
    meeting_list_title_loc = "android.widget.TextView"
    meeting_lists_loc =  "com.Meeting.itc.paperless:id/ll_meeting_item_view"

    def meeting_list_title(self):
        return self.by_id(self.meeting_list_title_loc)

    def meeting_lists(self):
        return self.by_ids(self.meeting_lists_loc)[0]


