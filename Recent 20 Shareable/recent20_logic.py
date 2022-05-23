from Objects import recent20_objects

most_recent_20 = "33hHpD2547qf39434V8QEo"
literally_everything = "2Z4gcXJCAWMgSDeynAzg2r"

playlist1_info = recent20_objects.GetPlaylistTracks(literally_everything, -20)
playlist2_info = recent20_objects.GetPlaylistTracks(most_recent_20, -20)


playlist1_info.get_playlist_items()
playlist2_info.get_playlist_items()

comparison = recent20_objects.URIid(literally_everything, playlist1_info.track_list, playlist1_info.uri_list, most_recent_20, playlist2_info.track_list, playlist2_info.uri_list)

comparison.get_uris_to_add()
comparison.get_uris_to_remove()
comparison.add_uris()
comparison.remove_uris()