# -*- coding: utf-8 -*-

# Module to handle i18n

import os
import gettext

# Initialize gettext
gettext_domain = 'turpial'
# localedir definition in development mode
if os.path.isdir(os.path.join(os.path.dirname(__file__), '..', 'i18n')):
    localedir = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'i18n'))
    trans = gettext.install(gettext_domain, localedir, unicode=1)
else:
    trans = gettext.install(gettext_domain, unicode=1)

STRINGS = {
    'welcome': _('Welcome!'),
    'twitter': 'Twitter',
    'identica': 'Identi.ca',
    'add_new_account': _('Add a new account'),
    'to_start_using_turpial': _('to start using Turpial'),
    'you_have_accounts_registered': _('You have accounts registered, now'),
    'add_some_columns': _('add some columns'),
    'update_status': _('Update status'),
    'send_direct_message': _('Send direct message'),
    'settings': _('Settings'),
    'preferences': _('Preferences'),
    'about_turpial': _('About Turpial'),
    'search': _('Search'),
    'account': _('Account'),
    'accounts': _('Accounts'),
    'columns': _('Columns'),
    'authorize_turpial': _('Authorize Turpial'),
    'type_the_pin': _('Type the PIN'),
    'save': _('Save'),
    'copy_the_pin': _('Authorize Turpial and copy the PIN in the text box'),
    'user_profile': _("User Profile"),
    'bio': _("Bio"),
    'location': _("Location"),
    'web': _("Web"),
    'tweets': _('Tweets'),
    'following': _('Following'),
    'followers': _('Followers'),
    'favorites': _('Favorites'),
    'criteria': _('Criteria'),
    'criteria_tooltip': _('Use hashtags, mentions or any text you want as search criteria'),
    'select_friend_to_send_message': _('Select friend to send message'),
    'friend': _('Friend'),
    'select': _('Select'),
    'load_friends_list': _('Load friends list'),
    'whats_happening': _("What's happening?"),
    'upload_image': _("Upload image"),
    'short_urls': _("Short URLs"),
    'update': _('Update'),
    'delete_column': _("Delete Column"),
    'now': _("now"),
    'retweeted_by': _("Retweeted by"),
    'new': _('New'),
    'delete': _('Delete'),
    'relogin': _('Relogin'),
    'register_a_new_account': _('Register a new account'),
    'delete_an_existing_account': _('Delete an existing account'),
    'register_a_twitter_account': _('Register a Twitter account'),
    'register_an_identica_account': _('Register an Identi.ca account'),
    'no_registered_accounts': _('No registered accounts'),
    'problems_registering_new_account': _('Problems registering a new account'),
    'broadcast': _('Broadcast'),
    'you_can_not_submit_an_empty_message': _("You can not submit an empty message"),
    'message_too_long': _("Hey! That message is too long, it looks like a testament"),
    'view_conversation': _("View conversation"),
    'hide_conversation': _("Hide conversation"),
    'reply': _('Reply'),
    'quote': _('Quote'),
    'retweet': _('Retweet'),
    'mark_as_favorite': _('Mark as favorite'),
    'remove_from_favorites': _('Remove from favorites'),
    'reply_to': _('Reply to'),
    'quoting': _('Quoting'),
    'confirm_retweet': _('Confirm Retweet'),
    'do_you_want_to_retweet_status': _('Do you want to retweet this status to all your friends?'),
    'confirm_delete': _('Confirm Delete'),
    'do_you_want_to_delete_status': _('Do you want to delete this status?'),
    'do_you_want_to_delete_direct_message': _('Do you want to delete this direct message?'),
    'loading': _('Loading...'),
    'status_repeated': _('Status repeated'),
    'status_deleted': _('Status deleted'),
    'direct_message_deleted': _('Direct message deleted'),
    'status_marked_as_favorite': _('Status marked as favorite'),
    'status_removed_from_favorites': _('Status removed from favorites'),
    'send_message_to': _('Send message to'),
    'follow': _('Follow'),
    'follow_requested': _('Follow requested'),
    'unfollow': _('Unfollow'),
    'mute': _("Mute"),
    'unmute': _("Unmute"),
    'block': _("Block"),
    'report_as_spam': _("Report as spam"),
    'this_is_you': _("This is you!"),
    'conversation': _("Conversation"),
    'quit': _('Quit'),
    'in_progress': _("In progress..."),
    'select_an_account_before_post': _("Select an account before post"),
    'image_preview': _("Image Preview"),
    'confirm_discard': _('Confirm Discard'),
    'do_you_want_to_discard_message': _('Do you want to discard this message?'),
    'info': _('Info'),
    'recent': _('Recent'),
    'delete_account_confirm': _("Do you really want to delete the account %s?"),
    'messages_queue': _('Messages queue'),
    'delete_selected_message': _('Delete selected message'),
    'delete_all': _('Delete all'),
    'delete_all_messages_in_queue': _('Delete all messages in queue'),
    'message': _('Message'),
    'delete_message_from_queue_confirm': _('Do you want to delete this message from the queue?'),
    'clear_message_queue_confirm': _('Do you want to clear the queue?'),
    'messages_will_be_send': _('Messages will be send every %s as long as Turpial remain open'),
    'next_message_should_be_posted_in': _('Next message should be posted in'),
    'minute': _("minute"),
    'minutes': _("minutes"),
    'add_to_queue': _('Add to Queue'),
    'about_description': _('Microblogging client written in Python'),
    'you_are_now_following': _("You are now following @%s"),
    'you_are_no_longer_following': _("You are no longer following @%s"),
    'has_been_reported_as_spam': _("@%s has been reported as spam"),
    'has_been_blocked': _("@%s has been blocked"),
    'has_been_muted': _("@%s has been muted"),
    'has_been_unmuted': _("@%s has been unmuted"),
    'message_from_queue_has_been_posted': _('Message from queue has been posted'),
    'close': _('Close'),
    'general': _('General'),
    'notifications': _('Notifications'),
    'services': _('Services'),
    'web_browser': _('Web Browser'),
    'filters': _('Filters'),
    'proxy': _('Proxy'),
    'advanced': _('Advanced'),
    'general_tab_description': _("Adjust update frecuency and other general parameters"),
    'notifications_tab_description': _("Select the notifications you want to receive from Turpial"),
    'web_browser_tab_description': _('Setup your favorite web browser to open links'),
    'services_tab_description': _("Select your preferred service to short URLs and upload images"),
    'proxy_tab_description': _("Proxy settings for Turpial (Need Restart)"),
    'advanced_tab_description': _("Advanced options. Please, keep away unless you know what you are doing"),
    'update_frecuency': _("Update frecuency"),
    'queue_frecuency': _("Queue frecuency"),
    'statuses_per_column': _("Statuses per column"),
    'minimize_on_close': _("Minimize on close"),
    'notify_on_updates': _("Notify on updates"),
    'notify_on_actions': _("Notify on actions"),
    'sound_on_login': _("Sound on login"),
    'sound_on_updates': _("Sound on updates"),
    'use_default_browser': _("Use default browser"),
    'set_custom_browser': _("Set custom browser"),
    'command': _("Command"),
    'clean_cache': _("Clean cache"),
    'delete_all_files_in_cache': _("Delete all files in cache"),
    'restore_config_to_default': _("Restore configuration to default"),
    'restore_config': _("Restore config"),
    'socket_timeout': _("Socket timeout"),
    'show_avatars': _("Show user avatars"),
    'type': _("Type"),
    'host': _("Host"),
    'port': _("Port"),
    'with_authentication': _("With authentication"),
    'username': _("Username"),
    'password': _("Password"),
    'filters': _("Filters"),
    'add_filter': _("Add filter"),
    'create_a_new_filter': _("Create a new filter"),
    'delete_selected_filter': _("Delete selected filter"),
    'delete_all_filters': _("Delete all filters"),
    'clear_filters_confirm': _('Do you want to clear all the filters?'),
    'error_loading_image': _("Error loading image"),
    'error_saving_image': _("Error saving image"),
    'error_loading_conversation': _("Error loading conversation"),
    'error_updating_column': _("Error updating column"),
    'error_repeating_status': _("Error repeating status"),
    'error_deleting_status': _("Error deleting status"),
    'error_marking_status_as_favorite': _("Error marking status as favorite"),
    'error_unmarking_status_as_favorite': _("Error unmarking status as favorite"),
    'error_posting_status': _("Error posting status"),
    'problems_loading_user_profile': _("Problems loading user profile"),
    'having_trouble_to_follow_user': _("Having some troubles to follow this user"),
    'having_trouble_to_unfollow_user': _("Having some troubles to unfollow this user"),
    'could_not_block_user': _("Uh oh, I could not block this user"),
    'having_issues_reporting_user_as_spam': _("Having issues reporting this user as spam"),
    'can_not_send_direct_message': _("Can not send direct message"),
    'error_shorting_url': _("Error shorting URL"),
    'error_uploading_image': _("Error uploading image"),
    'new_tweet_updated': _("1 new tweet updated"),
    'new_tweets_updated': _("%s new tweets updated"),
    'updated': _("%s updated"),
    'test': _("Test"),
    'open': _("Open"),
    'open_in_browser': _("Open in browser"),
    'update_frecuency_tooltip': _("Set how often are updated the columns"),
    'queue_frecuency_tooltip': _("Set how often are posted messages from the queue"),
    'minimize_on_close_tooltip': _("Send Turpial to system tray instead of closing"),
    'notify_on_updates_toolip': _("Display system notifications when you get updates"),
    'notify_on_actions_toolip': _("Display system notifications when you perform action like follow, block, etc"),
    'sound_on_login_tooltip': _("Play sounds at startup"),
    'sound_on_updates_tooltip': _("Play sounds when you get updates"),
    'socket_timeout_tooltip': _("Set the timeout to wait before closing the connection"),
    'show_avatars_tooltip': _("When selected Turpial show user avatars, Otherwise it will show a black box (recommended for slow or limited internet connections)"),
    'confirm_restore': _("Confirm restore"),
    'do_you_want_to_restore_config': _("Do you want to restore your configuration to default? Turpial will be closed and must be restarted after this operation"),
    'config_restored_successfully': _("Configuration restored to default successfully. Please, restart Turpial"),
    'that_account_does_not_exist': _("Wait! That account does not exist"),
    'hi_there': _("Hi there!"),
    'give_me_a_minute': _("Give me a minute, I am shaking my feathers and stretching my wings..."),
    'confirm_close': _("Confirm close"),
    'do_you_want_to_close_turpial': _("Do you want to close Turpial?"),
    'oh_oh': _("Uh oh..."),
    'something_terrible_happened': _("Something terrible happened, I could not reach the Internet"),
    'try_again': _("Try again"),
    'verify_image': _("Verify image"),
    'copy_image_url': _("Copy image URL"),
    'view_exif_info': _("View EXIF info"),
    'exif_data_not_available': _('EXIF data not available'),
    'show_hide': _("Show / Hide"),
}

class i18n:
    @staticmethod
    def get(key):
        try:
            return STRINGS[key]
        except KeyError:
            return key
