from Objects import recent20_objects_shareable

recent20_objects_shareable.playlist1_info = GetPlaylistTracks(literally_everything)
recent20_objects_shareable.playlist2_playlist2_info = GetPlaylistTracks(most_recent_20)


playlist1_info.get_playlist_items()
playlist2_info.get_playlist_items()

recent20_objects_shareable.comparison = URIid(literally_everything, playlist1_info.track_list, playlist1_info.uri_list, most_recent_20, playlist2_info.track_list, playlist2_info.uri_list)

comparison.get_uris_to_add()
comparison.get_uris_to_remove()
comparison.add_uris()
comparison.remove_uris()