from time import time, sleep

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

start_time = time()

results = get_pet_labels('pet_images/')

results=classify_images('pet_images/', results, 'alexnet')

results=adjust_results4_isadog(results, 'dognames.txt')

results_stats = calculates_results_stats(results)

print_results(results, results_stats, None, True, True)
    
# TODO 0: Measure total program runtime by collecting end time
end_time = time()
    
# TODO 0: Computes overall runtime in seconds & prints it in hh:mm:ss format
tot_time = end_time-start_time      #calculate difference between end time and start time
print("\n** Total Elapsed Runtime:",str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"+str(int((tot_time%3600)%60)) )

