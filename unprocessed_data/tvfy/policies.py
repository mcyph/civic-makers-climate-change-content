from enum import Enum, auto


class PolicyTypes(Enum):
    # What about cap 'n trade??
    CARBON_PRICE: 3
    RESOURCE_RENT: 14
    UNCONVENTIONAL_GAS_MINING: 18
    RENEWABLE_ENERGY_INVESTMENT: 20
    CARBON_FARMING: 33
    EMISSIONS_REDUCTION_FUND: 37
    URANIUM_EXPORT: 43

    # TODO: Finish this off+provde mappings to different datasets!!


policies = [
 {'description': 'the federal government should introduce a carbon pricing '
                 'mechanism',
  'id': 3,
  'name': 'a carbon price',
  'provisional': False},
 {'description': 'the federal government should introduce the Carbon Pollution '
                 'Reduction Scheme, which is a cap-and-trade system of '
                 'emissions trading introduced by the Rudd Labor Government',
  'id': 7,
  'name': 'the Carbon Pollution Reduction Scheme',
  'provisional': False},
 {'description': 'the federal government should put a tax on profits earned '
                 'from mining mineral resources such as coal and iron ore',
  'id': 14,
  'name': 'a minerals resource rent tax ',
  'provisional': False},
 {'description': 'the federal government should introduce legislation that '
                 "increases the protection of Australia's fresh water "
                 'resources, including its river and groundwater systems',
  'id': 15,
  'name': "increasing protection of Australia's fresh water",
  'provisional': False},
 {'description': 'the federal government should introduce legislation and '
                 "regulations that protect and conserve Australia's marine "
                 'ecosystems such as the Great Barrier Reef',
  'id': 17,
  'name': 'increasing marine conservation',
  'provisional': False},
 {'description': 'the federal government should allow companies to mine coal '
                 'seam (CSG), tight and shale gas',
  'id': 18,
  'name': 'unconventional gas mining',
  'provisional': False},
 {'description': 'the federal government should increase Aboriginal and Torres '
                 'Strait Islander land rights by, for example, increasing '
                 'their legal recognition and protection',
  'id': 24,
  'name': 'increasing Aboriginal land rights',
  'provisional': False},
 {'description': 'the federal government should allow live animal export and '
                 'place minimal restrictions on it',
  'id': 32,
  'name': 'live animal export',
  'provisional': False},
 {'description': 'the federal government should introduce a carbon farming '
                 'initiative that encourages the farming and timber industries '
                 'to decrease carbon emissions or to increase carbon storage '
                 '(known as carbon sequestration)',
  'id': 33,
  'name': 'carbon farming',
  'provisional': False},
 {'description': 'the federal government should introduce an emissions '
                 'reduction fund so it can buy domestic greenhouse gas '
                 'emissions reductions and offsets by reverse auction. This is '
                 "a key part of the Coalition Government's Direct Action "
                 'policy.',
  'id': 37,
  'name': 'an emissions reduction fund',
  'provisional': False},
 {'description': 'the federal government should provide more funding for road '
                 'infrastructure',
  'id': 38,
  'name': 'increasing funding for road infrastructure',
  'provisional': False},
 {'description': 'the federal government should increase fishing restrictions '
                 'so that fish populations are sustainable',
  'id': 41,
  'name': 'increasing fishing restrictions',
  'provisional': False},
 {'description': 'the federal government should encourage Australian-based '
                 'industry and secure the jobs these industries create by, for '
                 'example, providing incentives for companies to stay in '
                 'Australia',
  'id': 42,
  'name': 'encouraging Australian-based industry',
  'provisional': False},
 {'description': 'the federal government should support the exportation of '
                 'uranium from Australia',
  'id': 43,
  'name': 'uranium export',
  'provisional': False},
 {'description': 'The federal government should make its data and documents '
                 'more accessible for the general public and Parliament',
  'id': 59,
  'name': 'increasing accessibility of government data and documents',
  'provisional': False},
 {'description': 'landholders, particularly farmers, should be able to say no '
                 'to mining and gas exploration on their land (in other words, '
                 'they should be able to lock the gate)\r\n',
  'id': 62,
  'name': "landholders' right to say no to mining and gas exploration",
  'provisional': False},
 {'description': 'The Commonwealth create an agency with State and Local '
                 'Government advisors to process renewable energy projects '
                 'initiated by local communities to supply their energy needs '
                 'and store or sell surplus.\r\n'
                 'Depending on the environment this could be energy generation '
                 'from solar, wind or other sustainable projects. New jobs '
                 'would be generated for local residents to train and maintain '
                 'systems with the foresight of creating long-term '
                 'opportunities for young people.',
  'id': 64,
  'name': 'Cheaper, efficient, clean power generated locally and sometimes '
          'owned by the community.',
  'provisional': True},
 {'description': 'the federal government should address the causes and '
                 'consequences of climate change as a matter of urgency by, '
                 'for example, lowering emissions and investing in science and '
                 'technology',
  'id': 79,
  'name': 'treating government action on climate change as a matter of urgency',
  'provisional': False},
 {'description': 'environmental and conservation groups should be able to '
                 'challenge the legality of federal government decisions made '
                 'under the Environment Protection and Biodiversity '
                 'Conservation Act 1999 (EPBC Act) (in other words, they '
                 'should have standing to seek judicial review under that Act)',
  'id': 83,
  'name': 'letting environmental groups challenge the legality of certain '
          'government decisions',
  'provisional': False},
 {'description': 'the federal government should use the wealth generated by '
                 'mining for the benefit of Australian citizens, as encouraged '
                 'by the Extractive Industries Transparency Initiative (EITI) '
                 'Principles',
  'id': 88,
  'name': 'using natural resource wealth for the benefit of all Australians',
  'provisional': False},
 {'description': 'in light of the threat of climate change, the federal '
                 'government should make as rapid a transition to renewable '
                 'energy as possible',
  'id': 91,
  'name': 'a fast transition from fossil fuels to renewable energy',
  'provisional': False},
 {'description': 'the federal government should introduce legislation to end '
                 'illegal logging and prevent the importation of timber that '
                 'has been illegally harvested.',
  'id': 93,
  'name': 'ending illegal logging',
  'provisional': False},
 {'description': 'the federal government should protect threatened forest and '
                 'bushland habitats from logging.',
  'id': 94,
  'name': 'protecting threatened forest and bushland habitats',
  'provisional': False},
 {'description': 'the federal government should allocate 0.7% of Gross '
                 'National Income (GNI) to foreign aid in line with the United '
                 "Nations' target",
  'id': 99,
  'name': 'increasing the foreign aid budget to 0.7% of Gross National Income',
  'provisional': False},
 {'description': 'the federal government should always consult with local '
                 'communities that may be affected by infrastructure projects, '
                 'especially for major infrastructure projects such as dams, '
                 'pulp mills or nuclear facilities',
  'id': 102,
  'name': 'local community consultation on infrastructure projects',
  'provisional': False},
 {'description': 'the federal government should hold a plebiscite to gauge '
                 'whether citizens support or oppose introducing a carbon '
                 "pricing mechanism (also known as a 'carbon tax')",
  'id': 103,
  'name': 'a plebiscite on the carbon pricing mechanism',
  'provisional': False},
 {'description': 'the federal government should maintain or increase the '
                 'amount of funding allocated to the Commonwealth Scientific '
                 'and Industrial Research Organisation (CSIRO)',
  'id': 104,
  'name': 'maintaining or increasing CSIRO funding',
  'provisional': False},
 {'description': 'the federal government should take urgent action to address '
                 'the issue of rising sea levels',
  'id': 111,
  'name': 'addressing sea level rise as a matter of urgency',
  'provisional': True},
 {'description': 'there should be a high speed rail network connecting the '
                 'major cities on the east coast of Australia',
  'id': 115,
  'name': 'high speed rail on the east coast',
  'provisional': False},
 {'description': 'the federal government should make laws and regulations that '
                 'protect and conserve the health of the Great Barrier Reef '
                 'for future generations',
  'id': 122,
  'name': 'protecting the Great Barrier Reef',
  'provisional': False},
 {'description': 'the federal government should increase funding for public '
                 "transport within and between Australia's major urban centres "
                 'and prioritise it over funding for private transport '
                 'infrastructure projects',
  'id': 123,
  'name': 'public transport',
  'provisional': False},
 {'description': 'the federal government should create and coordinate a '
                 'National Redress Scheme for Survivors of Institutional '
                 'Sexual Abuse, which was recommended by the Royal Commission '
                 'into Institutional Responses to Child Sexual Abuse',
  'id': 125,
  'name': 'a national redress scheme for institutional abuse survivors',
  'provisional': False},
 {'description': 'the federal government should maintain and strengthen gun '
                 "control laws and make sure they're the same around Australia",
  'id': 126,
  'name': 'strengthening gun control laws',
  'provisional': False},
 {'description': 'the federal government should fund and maintain the '
                 'Australian Renewable Energy Agency, or ARENA, as an '
                 "independent body that manages the government's renewable "
                 'energy programs',
  'id': 127,
  'name': 'the Australian Renewable Energy Agency (ARENA)',
  'provisional': False},
 {'description': 'the federal government should protect the right of its '
                 'citizens to protest against its laws, policies and decisions',
  'id': 140,
  'name': 'the right to protest',
  'provisional': False},
 {'description': 'the federal government should maintain or increase its '
                 'investment in and support for the Australian coal industry',
  'id': 141,
  'name': 'increasing investment in the coal industry',
  'provisional': False},
 {'description': "the federal government's policies to reduce Australia's "
                 'greenhouse gas emissions should be "technology neutral", '
                 'which means all forms of electricity generation should be on '
                 'the table, including coal with carbon capture and storage '
                 'and gas',
  'id': 152,
  'name': 'technology neutral emission reduction targets',
  'provisional': False},
 {'description': 'all native title claimants need to sign an Indigenous Land '
                 'Use Agreement before the Agreement can be registered by the '
                 'Native Title Registrar (agreements like this let, for '
                 'example, mining companies mine in an area covered by native '
                 'title)',
  'id': 153,
  'name': 'requiring every native title claimant to sign land use agreements',
  'provisional': False},
 {'description': 'the federal government should give approval for new mines in '
                 'the Liverpool Plains, such as the Shenhua Watermark coal '
                 'mine',
  'id': 154,
  'name': 'giving approval for mining in the Liverpool Plains',
  'provisional': False},
 {'description': 'the federal government should keep up or increase the amount '
                 'of money it spends on defence',
  'id': 161,
  'name': 'maintaining or increasing defence spending',
  'provisional': False},
 {'description': "the federal government should support the Adani Group's "
                 "plans to build the Carmichael mine in Queensland's Galilee "
                 'Basin',
  'id': 162,
  'name': "Adani's proposed Carmichael coal mine in the Galilee Basin",
  'provisional': False},
 {'description': 'the federal government needs to support research and '
                 'conservation initiatives that aim to put a stop to the '
                 'current trajectory of animal and plant extinctions in '
                 'Australia',
  'id': 172,
  'name': 'government action on animal & plant extinctions',
  'provisional': False},
 {'description': 'the federal government should amend its laws and policies to '
                 'meet the objectives of the Paris Climate Agreement',
  'id': 183,
  'name': 'the Paris Climate Agreement',
  'provisional': False},
 {'description': 'the federal government should increase water allocations '
                 'from the Murray-Darling Basin for farmers and other users',
  'id': 185,
  'name': 'making more water from Murray-Darling Basin available to use',
  'provisional': False},
 {'description': 'the federal government should support nuclear energy '
                 'generation in Australia',
  'id': 196,
  'name': 'nuclear energy',
  'provisional': False},
 {'description': "the federal government should support MacMines' plans to "
                 "build the China Stone coal mine in Queensland's Galilee "
                 'Basin',
  'id': 201,
  'name': "MacMines' proposed China Stone coal mine in the Galilee Basin",
  'provisional': False},
 {'description': 'the federal government should increase their support of '
                 "Australia's dairy industry by, for example, regulating "
                 'increased milk prices',
  'id': 208,
  'name': 'increasing government support for the dairy industry',
  'provisional': False},
 {'description': 'the federal government should be required to seek the '
                 'consent of local communities before selecting new sites for '
                 'radioactive waste disposal',
  'id': 216,
  'name': 'community right to say no to nuclear waste disposal sites',
  'provisional': False},
 {'description': "the federal government should protect Australia's logging "
                 'industry and the jobs it represents',
  'id': 217,
  'name': "Australia's timber industry",
  'provisional': False},
 {'description': 'the federal government should put a ban on new thermal coal '
                 'mines opening in Australia',
  'id': 222,
  'name': 'banning new thermal coal mines',
  'provisional': False},
 {'description': 'the federal government should develop policies and '
                 'legislation that reduce air pollution, including vehicle '
                 'emissions',
  'id': 225,
  'name': 'reducing air pollution',
  'provisional': False},
 {'description': 'the federal government should invest in climate science to '
                 'ensure that Australia is best equipped to deal with the '
                 'challenges of climate change',
  'id': 227,
  'name': 'investing in climate science',
  'provisional': False},
 {'description': 'the federal government should invest in efforts to increase '
                 'community resilience to extreme weather events, such as '
                 'bushfires and floods',
  'id': 228,
  'name': 'building community climate change resilience',
  'provisional': False},
 {'description': 'the federal government should support offshore petroleum '
                 'mining by, for example, granting exploration and drilling '
                 'licences',
  'id': 231,
  'name': 'offshore oil mining',
  'provisional': False},
 {'description': 'the federal government should give greater environmental '
                 'approval powers to state and territory governments by '
                 'creating a single environmental assessment and approval '
                 'process for nationally protected matters that is '
                 'administered at state and territory level',
  'id': 245,
  'name': 'increasing state and territory environmental approval powers',
  'provisional': False},]


for policy in policies:
    print(f'{policy["id"]}\t{policy["name"]}\t{policy["name"]}\t{policy["description"]}')

