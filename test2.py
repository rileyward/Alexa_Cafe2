import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps


def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text(note, voice_pitch=voice_pitch, duration_scalar=0.6).wait_for_completed()
    voice_pitch = -1.0
    # SPEECH
    robot.say_text("Today I'm going to be talking about the social movement equal work for equal pay.", voice_pitch=voice_pitch,  duration_scalar=0.6).wait_for_completed()
    robot.say_text("Everyday, men and women do jobs that require equal skill and do not get equal pay.", voice_pitch=voice_pitch,  duration_scalar=0.6).wait_for_completed()
    robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    robot.say_text("Typically women get paid less than men for doing"
                   " the same amount of work. This gender discrimination is not fair.", voice_pitch=voice_pitch).wait_for_completed()
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
    robot.say_text("Companies should pay the same amount of money to all of their staff"
                   "that do the same job and do it to the same standards with the same skill set.", voice_pitch=voice_pitch).wait_for_completed()
    robot.say_text("This social movement is very important to me because this may effect me as an adult in lat"
                   "er life if we do not do something about it.", voice_pitch=voice_pitch).wait_for_completed()

cozmo.run_program(cozmo_program)