#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <utility>

int main() {
    std::vector<std::pair<std::string, std::string>> taggedSentence {
        {"The", "DT"},
        {"planet", "NN"},
        {"Jupiter", "NNP"},
        {"and", "CC"},
        {"its", "PPS"},
        {"moons", "NNS"},
        {"are", "VBP"},
        {"in", "IN"},
        {"effect", "NN"},
        {"a", "DT"},
        {"minisolar", "JJ"},
        {"system", "NN"},
        {",", ","},
        {"and", "CC"},
        {"Jupiter", "NNP"},
        {"itself", "PRP"},
        {"is", "VBZ"},
        {"often", "RB"},
        {"called", "VBN"},
        {"a", "DT"},
        {"star", "NN"},
        {"that", "IN"},
        {"never", "RB"},
        {"caught", "VBN"}, 
        {"fire", "NN"},
        {".", "."}
    };

    // Define contextual rules using a more structured approach
    struct TagRule {
        std::string prevTag;
        std::string nextTag;
        std::string resultTag;
    };
    
    // Rules for 2-letter missing tags
    std::vector<TagRule> twoLetterRules = {
        {"JJ", "", "NN"},
        {"DT", "", "JJ"},
        {"CC", "", "JJ"}
    };
    
    // Rules for 3-letter missing tags
    std::vector<TagRule> threeLetterRules = {
        {"VBP", "NN", "NNP"},
        {"IN", "NN", "NNP"},
        {"IN", "VBN", "PPS"}
    };

    // Fill in missing tags
    for (size_t i = 0; i < taggedSentence.size(); i++) {
        if (taggedSentence[i].second == "??") {
            // Apply two-letter rules
            for (const auto& rule : twoLetterRules) {
                if (i > 0 && taggedSentence[i-1].second == rule.prevTag) {
                    taggedSentence[i].second = rule.resultTag;
                    break;
                }
            }
        } else if (taggedSentence[i].second == "???") {
            // Apply three-letter rules
            for (const auto& rule : threeLetterRules) {
                if (i > 0 && i < taggedSentence.size() - 1 && 
                    taggedSentence[i-1].second == rule.prevTag && 
                    taggedSentence[i+1].second == rule.nextTag) {
                    taggedSentence[i].second = rule.resultTag;
                    break;
                }
            }
        }
    }

    // Print out the tagged sentence with filled-in missing tags
    for (const auto& token : taggedSentence) {
        std::cout << token.first << "/" << token.second << " ";
    }
    
    std::cout << std::endl;
    return 0;
}
