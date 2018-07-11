import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps


def cozmo_program(robot: cozmo.robot.Robot):
    voice_pitch = -1.0
    # SPEECH
    robot.say_text("Today I'm going to be talking about the social movement"
                   "equal work for equal pay.", voice_pitch=voice_pitch, duration_scalar=0.6).wait_for_completed()
    robot.say_text("Everyday, men and women do jobs that require equal skill and"
                   "do not get equal pay.", voice_pitch=voice_pitch, duration_scalar=0.6).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
    robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    robot.say_text("Typically women get paid less than men for doing"
                   "the same amount of work. This gender discrimination"
                   "is not fair.", voice_pitch=voice_pitch, duration_scalar=0.6).wait_for_completed()
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
    robot.say_text("Companies should pay the same amount of money to all of their staff"
                   "that do the same job and do it to the same standards with "
                   "the same skill set.", voice_pitch=voice_pitch, duration_scalar=0.6).wait_for_completed()
    robot.say_text("This social movement is very important to me because this "
                   "may effect me as an adult in later life if "
                   "we do not do something about it.", voice_pitch=voice_pitch, duration_scalar=0.6)\
        .wait_for_completed()
    # STACK DEMO
    # Lookaround until Cozmo knows win_place(degrees(90)).wait_for_completed()here at least 2 cubes are:
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes = robot.world.wait_until_observe_num_objects(num=2, object_type=cozmo.objects.LightCube, timeout=60)
    lookaround.stop()

    if len(cubes) < 2:
        print("Error: need 2 Cubes but only found", len(cubes), "Cube(s)")
    else:
        # Try and pickup the 1st cube
        current_action = robot.pickup_object(cubes[0], num_retries=5)
        current_action.wait_for_completed()
        if current_action.has_failed:
            code, reason = current_action.failure_reason
            result = current_action.result
            print("Pickup Cube failed: code=%s reason='%s' result=%s" % (code, reason, result))
            return

        # Now try to place that cube on the 2nd one
        current_action = robot.place_on_object(cubes[1], num_retries=5)
        current_action.wait_for_completed()
        if current_action.has_failed:
            code, reason = current_action.failure_reason
            result = current_action.result
            print("Place On Cube failed: code=%s reason='%s' result=%s" % (code, reason, result))
            return

    robot.say_text("Say person one was paid 20 dollars to "
                   "make this stack.", voice_pitch=voice_pitch, duration_scalar=0.3).wait_for_completed()
    # KNOCKDOWN STACK HERE

    # DEMO STACK 2
    # Look  around until Cozmo knows where at least 2 cubes are:
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes = robot.world.wait_until_observe_num_objects(num=2, object_type=cozmo.objects.LightCube, timeout=60)
    lookaround.stop()

    if len(cubes) < 2:
        print("Error: need 2 Cubes but only found", len(cubes), "Cube(s)")
    else:

        # Try and pickup the 1st cube
        current_action = robot.pickup_object(cubes[0], num_retries=5)
        current_action.wait_for_completed()
        if current_action.has_failed:
                code, reason = current_action.failure_reason
                result = current_action.result
                print("Pickup Cube failed: code=%s reason='%s' result=%s" % (code, reason, result))
                return

        # Now try to place that cube on the 2nd one
        current_action = robot.place_on_object(cubes[1], num_retries=5)
        current_action.wait_for_completed()
        if current_action.has_failed:
                code, reason = current_action.failure_reason
                result = current_action.result
                print("Place On Cube failed: code=%s reason='%s' result=%s" % (code, reason, result))
                return

    robot.say_text("And say another person was paid only 15 dollars to make the exact same stack."
                   "This person had the same skill set as person one but they only were"
                   "paid 15 dollars.", voice_pitch=voice_pitch, duration_scalar=0.6).wait_for_completed()

    robot.say_text("Thank you for listening.", voice_pitch=voice_pitch, duration_scalar=0.6).wait_for_completed()


cozmo.run_program(cozmo_program)
