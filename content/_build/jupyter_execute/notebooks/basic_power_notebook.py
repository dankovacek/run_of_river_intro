# How is Power and Energy Calculated for a Hydropower Project?

The power that can be generated from pressurized fluid in a pipeline is proportional to density ($\rho$), gravity ($g$), volumetric flow ($Q$), the electro-mechanical efficiency ($\zeta$), and the hydraulic head ($H_{net}$).

$$P = \rho g \zeta Q H_{net} $$

The **hydraulic head** is the elevation difference between the water level at the intake and the centreline elevation of the turbine, minus the losses in the pipeline due to friction.  

For a run-of-river hydropower project, the **flow** ($Q$) is governed by what is available in the river, minus what must be left in the river to maintain the aquatic ecosystem.  There is no storage, so the run-of-river plant can't be turned up or down to maximize revenue when demand (and thus price) is greatest.  On the other hand, the sediment that helps support the aquatic ecosystem in the diversion reach is not impeded in the same way as in a storage reservoir project.

The electro-mechanical efficiency is the friction loss in the conversion of rotational energy of the turbine runner to the movement of electric charges.  The total electro-mechanical efficiency is roughly 80-85% for a Pelton-type turbine-generator assembly.

## Example Calculation

First, let's take a look at an example calculation of power and energy. 

# assign constant variables
em_efficiency = 0.8 # dimensionless coefficient
density_water = 999 # kg/m^3
g = 9.81 # gravity, m/s^2

In a hydropower resource assessment, a project location of interest is assessed for many important characteristics, including:

* amount and timing of flow
* topology (slopes, waterfalls, etc.)
* sensitive ecosystems (ungulate wintering ranges, horned owl habitat, salmon spawning habitat, etc.)
* cultural valued components (sites of historical and cultural importance for First Nations)

The first two characteristics need to be characterized to determine how much power and energy can be generated.  The third and fourth can determine if an area is not suitable for development of a hydropower project.  

Returning to the power calculation: assume we are asked to assess a location for hydropower potential.  

1. The most cursory estimate of where we could build an intake and powerhouse yields an **elevation difference of 100m**.
2. A nearby river has been monitored for several decades by the [Water Survey of Canada](https://www.canada.ca/en/environment-climate-change/services/water-overview/quantity/monitoring/survey.html), and the most cursory calculation shows that on a **unit area** basis, the nearby catchment generates $75 \frac{L}{s \cdot km^2}$ on an average annual basis.
4. The **catchment area** at our first-guess intake location is $50 km^2$.
5. Set an initial target of 5% hydraulic losses

drainage_area = 50 # drainage area, km^2
unit_runoff = 75 # L/s/km^2
gross_head = 100 # 100 m elevation gain

# calculate net head
hydraulic_loss = 0.05  # 5% hydraulic losses
H_net = gross_head - hydraulic_loss * gross_head

Using the mean runoff from the nearby catchment, combined with an estimate of the drainage area **defined by our intake location**, we can make a first approximation of a mean annual discharge (MAD) for our project intake.  We can use this MAD as a first approximation for a design flow $Q$ for our hydro project.

First, we need to conver the unit area runoff $\frac{L}{s \cdot km^2}$ to volumetric flow $\frac{m^3}{s}$.

$$UR \left[ \frac{L}{s \cdot km^2} \right] \times A_{basin} [km^2] \div 1000 \left[ \frac{L}{m^3} \right] $$

Yields $\frac{m^3}{s}$

q_design = unit_runoff * drainage_area / 1000
q_design

Using the formula from above, calculate power.  *Always check units!!*

$$P = \rho g \zeta Q H_{net} $$

$$ = \left[ \frac{kg}{m^3} \right] \times \left[ \frac{m}{s^2} \right] \times [-] \times \left[ \frac{m^3}{s} \right] \times [ {m}]$$

Recall that the unit of force, the Newton $1 N = \left[ \frac{kg \cdot m}{s^2} \right] $.  Substituting into the above equation:

$$ = \left[ \frac{N}{m^3} \right] \times \left[ \frac{m^3}{s} \right] \times [ {m}]$$

Cancelling the volume $m^3$,

$$ = \left[ \frac{N\cdot m}{s} \right] $$

Recall that **work** (energy) is defined as a force applied over some distance ($W = F\times d$ expressed in units of Joules ($J$)), and Power is the rate of work per unit time ($\frac{J}{s}$), expressed in Watts ($1 \frac{J}{s} =  1 W$).  

So given the units our density, flow, head, etc. parameters are expressed in, the result will be Watts.

Also recall the following prefixes and their meanings:

| Prefix | Numeric Value | Power Unit |
|---|---|---|
| *kilo* | 1000 ($10^3$) | **kilo**Watt (kW) |
| *mega* | 1,000,000 ($10^6$) | **mega**Watt (MW) |
| *giga* | $10^9$ | **giga**Watt (GW) |
| *tera* | $10^12$ | **tera**Watt (TW) |



# Calculate Power

P = em_efficiency * density_water * g * q_design * H_net
# convert to MegaWatts
P_MW = P / 1E6
print(f'The estimated power is {P_MW:.1f} MW.')

## Estimate Energy

Given we've made a first approximation of power for our hypothetical hydro project, let's now make (an equally rough) estimate of how much energy we can make per year based on our design flow.  Let's use the term **Mean Annual Energy (MAE)** to describe how much energy what we might expect in an average year.  Above, we used the unit of work in Joules in deriving power, but in the energy industry, electric energy is typically expressed in **Watt hours** ($Wh$).

$$MAE = P \times t$$

# calculate hours in a year
t = 24 * 365
mae_MWh = P_MW * t

# convert MWh to GWh to make the number consistent with how it's expressed in industry
mae_GWh = mae_MWh / 1E3
print(f'The estimated annual energy is {mae_GWh:.0f} GWh.')

## Improving the Estimate

In the example above, we've made a very rough estimate of power and energy.  

1. What assumptions went into the parameters we used?
2. What can we do to make more accurate estimates?

