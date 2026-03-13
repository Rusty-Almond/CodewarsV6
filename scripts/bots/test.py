def run(state, memory):
    memory={

    }
    my_x,my_y=state.my_position()
    my_health=state.my_health()
    my_fuel=state.my_fuel()
    my_score=state.my_score()
    current_mag,reserve_ammo=state.my_ammo()
    aim_angle=state.my_aim_angle()
    gun=state.my_gun()
    enemies=state.enemy_positions()
    markers=state.player_markers()


    # SOME CONSTANTS

    GRENADE_ESCAPE_DIST=110


    # Run away from nades
    nades=state.active_grenades()
    nearest_nade = None
    nearest_nade_dist = 1e9 
    for g in nades :
        nx=float(g["x"])
        ny=float(g["y"])
        dist = math.sqrt((nx-my_x)**2 + (ny-my_y)**2)
        if dist < nearest_nade_dist:
            nearest_nade_dist=d
            nearest_nade=g

    if nearest_nade is not None and nearest_nade_dist < GRENADE_ESCAPE_DIST :
        