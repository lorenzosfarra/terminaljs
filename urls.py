 # Copyright (C) 2010 Lorenzo Sfarra (lorenzosfarra@ubuntu.com)
 #
 # This program is free software; you can redistribute it and/or
 # modify it under the terms of the GNU General Public License
 # as published by the Free Software Foundation; either version 2
 # of the License, or (at your option) any later version.
 #
 # This program is distributed in the hope that it will be useful,
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 # GNU General Public License for more details.
 #
 # You should have received a copy of the GNU General Public License
 # along with this program; if not, write to the Free Software
 # Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
 #


from django.conf.urls.defaults import *
from django.conf import settings

MEDIA_ROOT = settings.MEDIA_ROOT

urlpatterns = patterns('',
    (r'^cmd/(?P<command>.*)$', 'terminaljs.terminal.views.cmd'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                            {'document_root': MEDIA_ROOT}),
    (r'^$', 'terminaljs.terminal.views.index'),
)
